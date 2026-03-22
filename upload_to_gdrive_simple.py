#!/usr/bin/env python3
"""
Simple Google Drive Video Uploader using Service Account
Works in GitHub Actions with service account credentials
"""

import os
import sys
from pathlib import Path
import logging
import json

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    HAS_GOOGLE_API = True
except ImportError:
    HAS_GOOGLE_API = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# Base path (relative for GitHub Actions compatibility)
BASE_PATH = Path(__file__).parent.resolve()
OUTPUT_VIDEOS_FOLDER = BASE_PATH / "output"

# Import language config from download script to keep IDs in sync
import sys
sys.path.insert(0, str(BASE_PATH))
try:
    from download_from_gdrive import GoogleDriveDownloader
    LANGUAGE_CONFIG = {}
    for lang, config in GoogleDriveDownloader.LANGUAGE_CONFIG.items():
        LANGUAGE_CONFIG[lang] = {
            'code': config['code'],
            'output_folder_id': config.get('video_folder_id', '')
        }
except ImportError:
    # Fallback if import fails
    logger.warning("⚠️  Could not import config from download script, using defaults")
    LANGUAGE_CONFIG = {
        'ENGLISH': {'code': 'GGENG', 'output_folder_id': ''},
        'KANNADA': {'code': 'GGKND', 'output_folder_id': ''},
        'TELUGU': {'code': 'GGTLG', 'output_folder_id': ''},
        'HINDI': {'code': 'GGHND', 'output_folder_id': ''},
        'MARATHI': {'code': 'GGMRT', 'output_folder_id': ''},
        'TAMIL': {'code': 'GGTML', 'output_folder_id': ''},
    }


def get_drive_service():
    """Create Google Drive service using service account credentials"""
    
    if not HAS_GOOGLE_API:
        logger.error("❌ Google API client not installed")
        logger.error("📦 Install: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client")
        sys.exit(1)
    
    # Check for service account credentials
    creds_json = os.getenv('GOOGLE_SERVICE_ACCOUNT_KEY')
    
    if not creds_json:
        logger.error("❌ GOOGLE_SERVICE_ACCOUNT_KEY environment variable not set")
        logger.error("💡 Set up instructions:")
        logger.error("   1. Go to https://console.cloud.google.com/")
        logger.error("   2. Create a service account")
        logger.error("   3. Download JSON key")
        logger.error("   4. Add as GitHub secret: GOOGLE_SERVICE_ACCOUNT_KEY")
        sys.exit(1)
    
    try:
        # Parse service account credentials
        creds_data = json.loads(creds_json)
        credentials = service_account.Credentials.from_service_account_info(
            creds_data,
            scopes=['https://www.googleapis.com/auth/drive.file']
        )
        
        # Build Drive service
        service = build('drive', 'v3', credentials=credentials)
        return service
        
    except Exception as e:
        logger.error(f"❌ Failed to create Drive service: {e}")
        sys.exit(1)


def detect_language(filename):
    """Detect language from filename prefix"""
    for lang, config in LANGUAGE_CONFIG.items():
        if filename.startswith(config['code']):
            return lang
    return None


def upload_file(service, file_path, folder_id, filename):
    """Upload a file to Google Drive folder"""
    
    try:
        file_metadata = {
            'name': filename,
            'parents': [folder_id]
        }
        
        media = MediaFileUpload(
            str(file_path),
            mimetype='video/mp4',
            resumable=True
        )
        
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id,name,webViewLink'
        ).execute()
        
        logger.info(f"   ✅ Uploaded: {filename}")
        logger.info(f"      Link: {file.get('webViewLink', 'N/A')}")
        
        return True
        
    except Exception as e:
        logger.error(f"   ❌ Failed to upload {filename}: {e}")
        return False


def main():
    """Main upload function"""
    
    logger.info("="*60)
    logger.info("📤 Google Drive Video Uploader (Service Account)")
    logger.info("="*60)
    
    # Get language from command line
    language = None
    if len(sys.argv) > 1:
        language = sys.argv[1].upper()
    
    # Check output folder
    if not OUTPUT_VIDEOS_FOLDER.exists():
        logger.error(f"❌ Output folder not found: {OUTPUT_VIDEOS_FOLDER}")
        sys.exit(1)
    
    # Get video files
    video_files = list(OUTPUT_VIDEOS_FOLDER.glob('*.mp4'))
    
    if not video_files:
        logger.warning("⚠️  No video files found")
        sys.exit(0)
    
    logger.info(f"\n📁 Found {len(video_files)} video files\n")
    
    # Filter by language if specified
    if language:
        video_files = [f for f in video_files if detect_language(f.name) == language]
        logger.info(f"🔍 Filtering for {language}: {len(video_files)} files\n")
    
    if not video_files:
        logger.warning(f"⚠️  No {language} videos found")
        sys.exit(0)
    
    # Create Drive service
    service = get_drive_service()
    
    # Upload videos by language
    success_count = 0
    failed_count = 0
    
    for video_file in video_files:
        lang = detect_language(video_file.name)
        
        if not lang:
            logger.warning(f"⚠️  Skipping {video_file.name} (unknown language)")
            continue
        
        folder_id = LANGUAGE_CONFIG[lang]['output_folder_id']
        
        if not folder_id:
            logger.error(f"❌ No output folder configured for {lang}")
            logger.error(f"   Set environment variable: {lang}_VIDEO_FOLDER_ID")
            failed_count += 1
            continue
        
        logger.info(f"📤 Uploading {lang}: {video_file.name}")
        
        if upload_file(service, video_file, folder_id, video_file.name):
            success_count += 1
        else:
            failed_count += 1
    
    # Summary
    logger.info("\n" + "="*60)
    logger.info("📊 Upload Summary")
    logger.info("="*60)
    logger.info(f"✅ Successful: {success_count}")
    logger.info(f"❌ Failed: {failed_count}")
    logger.info(f"📁 Total: {success_count + failed_count}")
    logger.info("="*60)
    
    sys.exit(0 if failed_count == 0 else 1)


if __name__ == '__main__':
    main()
