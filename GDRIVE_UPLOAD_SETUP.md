# Google Drive Auto-Upload Setup Guide

This guide shows you how to enable automatic uploading of generated videos to Google Drive so your team can access them without GitHub login.

## 📋 Overview

Once configured, videos will automatically upload to Google Drive after generation, organized by language folder.

## 🚀 Setup Steps

### Step 1: Get Video Folder IDs from Google Drive

1. Go to your Google Drive: **Srisatupasi > GG ENGLISH** (or any language)

2. Find or create the folder where videos should be uploaded:
   - Example: `ENGLISH video files/` or `Generated ENGLISH Videos/`

3. Right-click the folder → **Share** → **Get link**
4. From the link like this:
   ```
   https://drive.google.com/drive/folders/1xYz123AbC456DeF789GhI
   ```
5. Extract just the folder ID:

   ```
   1xYz123AbC456DeF789GhI
   ```

6. **Repeat for all 6 languages** (ENGLISH, KANNADA, HINDI, TAMIL, TELUGU, MARATHI)

7. Make sure each folder is shared with **"Anyone with the link can view"**

### Step 2: Add Folder IDs to Config

Edit `download_from_gdrive.py` around line 68:

```python
LANGUAGE_CONFIG = {
    'ENGLISH': {
        'code': 'GGENG',
        'images_folder_id': '1WM3BmU46pRya1ZloxZJ---HbU_phALlZ',
        'audio_folder_id': '1luI0MuvI5NnRh8Oh-0b6NWAJ8SAaWU2R',
        'video_folder_id': '1xYz123AbC456DeF789GhI',  # ← PASTE YOUR VIDEO FOLDER ID HERE
        'digits': 3
    },
    'KANNADA': {
        'code': 'GGKND',
        'images_folder_id': '1nuuHeJskv5ljtw3oT7y_yHRLalk51A6I',
        'audio_folder_id': '197ef6kJre8snZiiMK_lurgw2N--CE2is',
        'video_folder_id': 'YOUR_KANNADA_VIDEO_FOLDER_ID',  # ← ADD THIS
        'digits': 3
    },
    # ... repeat for all languages
}
```

### Step 3: Create Google Service Account

1. Go to [Google Cloud Console](https://console.cloud.google.com/)

2. Create a new project (or select existing):
   - Name: `video-generator` or similar
   - Click **CREATE**

3. Enable Google Drive API:
   - Go to **APIs & Services** → **Library**
   - Search for "Google Drive API"
   - Click **ENABLE**

4. Create Service Account:
   - Go to **APIs & Services** → **Credentials**
   - Click **+ CREATE CREDENTIALS** → **Service account**
   - Name: `github-actions-uploader`
   - Description: `Uploads videos from GitHub Actions`
   - Click **CREATE AND CONTINUE**
   - Skip roles (click **CONTINUE**)
   - Click **DONE**

5. Create JSON Key:
   - Click on the service account you just created
   - Go to **KEYS** tab
   - Click **ADD KEY** → **Create new key**
   - Choose **JSON**
   - Click **CREATE**
   - A JSON file will download - **keep this safe!**

6. Get the service account email:
   - Copy the email address (looks like: `github-actions-uploader@video-generator-xxxxx.iam.gserviceaccount.com`)

### Step 4: Share Google Drive Folders with Service Account

For **each language video folder** (all 6):

1. Go to the folder in Google Drive
2. Right-click → **Share**
3. Paste the service account email
4. Set permission to **Editor**
5. Uncheck "Notify people"
6. Click **Share**

### Step 5: Add Secret to GitHub

1. Open the downloaded JSON key file in a text editor

2. Copy the **entire contents** (should start with `{` and end with `}`)

3. Go to your GitHub repository:
   - https://github.com/srisatupasi2498/image_audio_video_maker

4. Go to **Settings** → **Secrets and variables** → **Actions**

5. Click **New repository secret**

6. Name: `GOOGLE_SERVICE_ACCOUNT_KEY`

7. Value: Paste the entire JSON content

8. Click **Add secret**

## ✅ Test the Setup

1. Commit and push your config changes:

   ```bash
   git add download_from_gdrive.py
   git commit -m "Add video folder IDs for Google Drive upload"
   git push
   ```

2. Trigger a test workflow from the web form:
   - Go to: https://srisatupasi2498.github.io/image_audio_video_maker/
   - Select a language with both images and audio
   - Submit

3. Check the workflow logs:
   - Look for "📤 Upload Videos to Google Drive" step
   - Should show: "✅ Uploaded: GGENG012.mp4" with a Google Drive link

4. Verify in Google Drive:
   - Go to your language video folder
   - Videos should appear there automatically!

## 🔍 Troubleshooting

### Upload step is skipped

- Make sure you added the `GOOGLE_SERVICE_ACCOUNT_KEY` secret to GitHub
- Check that the secret name matches exactly (case-sensitive)

### "No output folder configured"

- Add `video_folder_id` to the language config in `download_from_gdrive.py`
- Push the changes to GitHub

### "Permission denied" or "403 Forbidden"

- Make sure you shared each video folder with the service account email
- Give it **Editor** permission (not Viewer)

### Videos don't appear in Google Drive

- Check the workflow logs for the Google Drive link
- Verify the folder ID is correct
- Make sure the folder is shared with the service account

## 📊 What Your Team Will See

After setup, your team can:

1. Go to the language folder in Google Drive (e.g., "GG ENGLISH/ENGLISH video files/")
2. See newly generated videos appear automatically after each workflow
3. Download/share videos directly from Google Drive
4. No GitHub account needed! ✨

## 🔐 Security Notes

- The service account key is stored securely in GitHub Secrets
- Only has access to folders you explicitly share with it
- Can only upload files, not delete or modify existing ones
- Key never appears in logs or outputs

## 📝 Keeping Things Organized

Recommended folder structure in Google Drive:

```
Srisatupasi/
├── GG ENGLISH/
│   ├── ENGLISH jpg files/          (existing - for downloads)
│   ├── Final ENGLISH audio files/  (existing - for downloads)
│   └── Generated ENGLISH Videos/   (new - for uploads) ← Get this ID
├── GG KANNADA/
│   ├── KANNADA jpg files/
│   ├── Final KANNADA audio files/
│   └── Generated KANNADA Videos/   ← Get this ID
└── ... (repeat for all languages)
```
