# 🎬 Video Generator - Production Setup Guide

## Overview

This system now supports **multiple projects** and uses a **flexible configuration file** instead of hardcoded values.

---

## 📋 Quick Summary of Improvements

### ✅ **1. Direct Download Link**
- Form now shows a direct link to download videos
- Auto-redirects to workflow page after 3 seconds
- Clear instructions on where to find artifacts

### ✅ **2. Configuration File (`config.json`)**
- All Google Drive folder IDs are now in `config.json`
- Easy to change without touching code
- Support for multiple projects

### ✅ **3. Multi-Project Support**
- Can handle different naming patterns (not just "GG" prefix)
- Switch between projects by changing `active_project` in config
- Each project can have its own folder structure

---

## 🔧 Configuration Setup

### Option 1: Using config.json (Current - Simple)

Edit `/Users/vkuma153/video_generator/image_audio_video_maker/config.json`:

```json
{
  "projects": {
    "GuruGeeta": {
      "file_prefix_pattern": "GG{LANG_CODE}",
      "languages": {
        "ENGLISH": {
          "code": "ENG",
          "images_folder_id": "YOUR_FOLDER_ID_HERE",
          "audio_folder_id": "YOUR_FOLDER_ID_HERE"
        }
      }
    },
    "AnotherProject": {
      "file_prefix_pattern": "AP{LANG_CODE}",
      "languages": {
        "ENGLISH": {
          "code": "ENG",
          "images_folder_id": "DIFFERENT_FOLDER_ID",
          "audio_folder_id": "DIFFERENT_FOLDER_ID"
        }
      }
    }
  },
  "active_project": "GuruGeeta"
}
```

### Option 2: Using GitHub Repository Variables (Production - Recommended)

For production, use GitHub repository variables to avoid committing folder IDs:

1. **Go to Repository Settings:**
   ```
   https://github.com/srisatupasi2498/image_audio_video_maker/settings/variables/actions
   ```

2. **Create Variables:**
   - `GG_ENGLISH_IMAGES_FOLDER_ID` = `1WM3BmU46pRya1ZloxZJ---HbU_phALlZ`
   - `GG_ENGLISH_AUDIO_FOLDER_ID` = `1luI0MuvI5NnRh8Oh-0b6NWAJ8SAaWU2R`
   - `GG_KANNADA_IMAGES_FOLDER_ID` = `...`
   - And so on for each language

3. **Update workflow** to pass these as environment variables

---

## 🎯 How to Add a New Project

### Example: Adding "Bhagavad Gita" Project

1. **Edit `config.json`:**

```json
{
  "projects": {
    "GuruGeeta": { ... },
    "BhagavadGita": {
      "file_prefix_pattern": "BG{LANG_CODE}",
      "languages": {
        "ENGLISH": {
          "code": "ENG",
          "images_folder_id": "NEW_FOLDER_ID_HERE",
          "audio_folder_id": "NEW_FOLDER_ID_HERE",
          "digits": 3
        },
        "HINDI": {
          "code": "HND",
          "images_folder_id": "NEW_FOLDER_ID_HERE",
          "audio_folder_id": "NEW_FOLDER_ID_HERE",
          "digits": 3
        }
      }
    }
  },
  "active_project": "BhagavadGita"  // ← Switch active project
}
```

2. **File naming will automatically be:**
   - `BGENG001.jpg`, `BGENG001.mp3` (English)
   - `BGHND001.jpg`, `BGHND001.mp3` (Hindi)

3. **Commit and push:**
```bash
git add config.json
git commit -m "Add Bhagavad Gita project"
git push origin main
```

---

## 📥 How Team Members Download Videos

After triggering video generation:

1. **Click the blue button** that appears after submitting the form
2. **OR** manually go to: `https://github.com/srisatupasi2498/image_audio_video_maker/actions`
3. **Click on the latest workflow run** (top of the list)
4. **Wait for green checkmark** (✓) - takes ~15-20 minutes
5. **Scroll down to "Artifacts"** section
6. **Click to download** `generated-videos-LANGUAGE-START-END.zip`
7. **Unzip** and find videos in the `output/` folder

---

## 🚀 Next Steps (Optional Enhancements)

### For Full Production:

1. **Move folder IDs to GitHub Variables** (more secure)
2. **Add Google Drive upload** (requires OAuth setup)
3. **Email notifications** when videos are ready
4. **Custom domain** for GitHub Pages
5. **Usage tracking** and analytics

---

## 📞 Support

For issues or questions, contact the repository maintainer.

**Repository:** https://github.com/srisatupasi2498/image_audio_video_maker
**Web Form:** https://srisatupasi2498.github.io/image_audio_video_maker/
