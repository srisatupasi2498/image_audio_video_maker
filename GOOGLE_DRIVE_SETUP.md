# Google Drive Upload Setup Guide

This guide explains how to enable automatic video upload to Google Drive using a service account.

## Overview

The system can automatically upload generated videos to your Google Drive folders using **Service Account** authentication, which works perfectly in GitHub Actions without requiring manual OAuth login.

## Setup Steps

### 1. Create Google Cloud Project (5 minutes)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" → "NEW PROJECT"
3. Name it: `video-generator-automation`
4. Click "CREATE"

### 2. Enable Google Drive API (1 minute)

1. From the project dashboard, go to "APIs & Services" → "Enable APIs and Services"
2. Search for "Google Drive API"
3. Click on it and click "ENABLE"

### 3. Create Service Account (3 minutes)

1. Go to "APIs & Services" → "Credentials"
2. Click "CREATE CREDENTIALS" → "Service Account"
3. Fill in details:
   - **Service account name**: `video-uploader`
   - **Service account ID**: (auto-generated)
   - **Description**: `Automated video upload service`
4. Click "CREATE AND CONTINUE"
5. Skip "Grant this service account access to project" (click CONTINUE)
6. Skip "Grant users access to this service account" (click DONE)

### 4. Generate Service Account Key (2 minutes)

1. In the Credentials page, find your service account
2. Click on the service account email
3. Go to "KEYS" tab
4. Click "ADD KEY" → "Create new key"
5. Choose **JSON** format
6. Click "CREATE"
7. Save the downloaded JSON file securely (you'll use this next)

### 5. Share Google Drive Folders (5 minutes)

You need to share each language's video output folder with the service account:

1. Open your Google Drive
2. Navigate to each video output folder (e.g., `Srisatupasi/GG ENGLISH/Generated Videos`)
3. Right-click the folder → "Share"
4. Add the service account email (found in the JSON file, looks like `video-uploader@video-generator-automation.iam.gserviceaccount.com`)
5. Give **Editor** permission
6. Click "Share"
7. Repeat for all 6 language folders

### 6. Get Folder IDs (3 minutes)

For each shared folder, get the folder ID:

1. Open the folder in Google Drive
2. Look at the URL: `https://drive.google.com/drive/folders/FOLDER_ID_HERE`
3. Copy the `FOLDER_ID_HERE` part
4. Save these IDs for the next step

### 7. Add GitHub Secrets (5 minutes)

1. Go to your GitHub repository: `https://github.com/srisatupasi2498/image_audio_video_maker`
2. Click "Settings" → "Secrets and variables" → "Actions"
3. Click "New repository secret" for each of these:

**Service Account Key:**
- Name: `GOOGLE_SERVICE_ACCOUNT_KEY`
- Value: Open the JSON file you downloaded, copy the ENTIRE contents, paste it

**Folder IDs for each language:**
- Name: `ENGLISH_VIDEO_FOLDER_ID`
- Value: (paste the folder ID from step 6)

- Name: `KANNADA_VIDEO_FOLDER_ID`
- Value: (paste the folder ID)

- Name: `TELUGU_VIDEO_FOLDER_ID`
- Value: (paste the folder ID)

- Name: `HINDI_VIDEO_FOLDER_ID`
- Value: (paste the folder ID)

- Name: `MARATHI_VIDEO_FOLDER_ID`
- Value: (paste the folder ID)

- Name: `TAMIL_VIDEO_FOLDER_ID`
- Value: (paste the folder ID)

### 8. Update requirements.txt

The workflow needs these Python packages:
```
google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
```

These will be added automatically when you update the workflow.

## Testing

After setup, test the upload:

1. Trigger video generation from the web form
2. Wait for generation to complete
3. Check the workflow logs for upload success
4. Verify videos appear in your Google Drive folders

## Security Notes

✅ **Safe:**
- Service account has limited permissions (only Drive API)
- JSON key is stored as GitHub secret (encrypted)
- Only shares specific folders, not entire Drive

⚠️ **Important:**
- Never commit the service account JSON file to git
- Don't share the JSON key publicly
- Keep GitHub secrets protected

## Troubleshooting

### "Permission denied" error
→ Make sure you shared the folder with the service account email

### "Folder not found" error
→ Check that folder IDs are correct in GitHub secrets

### "API not enabled" error
→ Enable Google Drive API in Google Cloud Console

### Upload is slow
→ Normal for large videos. GitHub Actions has good bandwidth.

## Cost

**FREE** ✅
- Google Cloud free tier includes Drive API usage
- No charges for reasonable video upload volumes
- GitHub Actions free tier: 2,000 minutes/month

## Alternative: Artifact Download Only

If you prefer NOT to set up Google Drive upload:
- Videos will still be available as **GitHub Artifacts**
- Download from workflow page after generation
- Artifacts expire after 30 days
- No Google Cloud setup needed

Simply don't enable the upload step in the workflow.
