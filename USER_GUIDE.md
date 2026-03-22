# 🌐 Video Generator - User Guide

**Generate videos effortlessly with our web interface!**

---

## 🚀 Quick Start (3 Steps)

### **Step 1:** Open the Web App

🔗 **[https://srisatupasi2498.github.io/image_audio_video_maker/](https://srisatupasi2498.github.io/image_audio_video_maker/)**

---

### **Step 2:** Fill the Form

| Field            | Example   | Description                                                  |
| ---------------- | --------- | ------------------------------------------------------------ |
| **Language**     | `ENGLISH` | Select from: ENGLISH, KANNADA, HINDI, TAMIL, TELUGU, MARATHI |
| **Start Number** | `12`      | First file number (e.g., 12 for GGENG012)                    |
| **End Number**   | `14`      | Last file number (e.g., 14 for GGENG014)                     |

---

### **Step 3:** Click "Generate Videos"

That's it! ✨ The workflow starts immediately and videos will appear in your Google Drive.

---

## ⏱️ What Happens Next?

1. ⚙️ **GitHub Actions starts** (workflow begins in cloud)
2. 📥 **Downloads media** (~2-5 min): Fetches images/audio from Google Drive
3. 🎬 **Generates videos** (~10-15 min): Creates 1080p MP4 files with background music
4. 📤 **Uploads to Google Drive** (~1-2 min): Videos appear automatically
5. 📦 **Creates backup artifacts** (available for 30 days)

**Total Time:** ~15-25 minutes

---

## 📊 Monitor Progress

The web page automatically tracks your workflow:

- 🟡 **Running** - Workflow in progress (updates every 30 seconds)
- ✅ **Completed** - Videos ready!
- ❌ **Failed** - Check workflow logs for details

**Advanced Monitoring:**

Click **"View All Workflows & Downloads"** button to see all runs and download artifacts.

---

## 📂 Access Your Videos

### Primary Method: Google Drive (Recommended) 🎉

Videos automatically appear in your Google Drive:

**Path:** `Srisatupasi > GG [LANGUAGE] > [LANGUAGE] video files/`

**Examples:**

- English: `Srisatupasi > GG ENGLISH > ENGLISH video files/`
- Kannada: `Srisatupasi > GG KANNADA > KANNADA video files/`

**✨ No GitHub login required!** Your entire team can access videos directly from Google Drive.

---

### Backup Method: GitHub Artifacts

If needed, you can also download from GitHub:

1. Click **"View All Workflows"** on the web page
2. Find your workflow run (look for language and number range)
3. Scroll down to **"Artifacts"** section
4. Download the ZIP file
5. Extract to get MP4 files

**Note:** Artifacts expire after 30 days, but Google Drive videos stay forever.

---

## 🔄 Running Multiple Workflows

You can generate videos for different languages/ranges simultaneously:

1. Submit first request (e.g., ENGLISH 1-10)
2. **Immediately submit another** (e.g., KANNADA 5-15)
3. Both run in parallel!
4. Each workflow is tracked independently

**Tip:** Use the "View All Workflows" button to monitor all parallel runs.

---

## ❓ Common Questions

### Q: How long do videos take?

**A:** 15-25 minutes depending on the number of files.

### Q: Can I generate while another is running?

**A:** Yes! Multiple workflows run in parallel.

### Q: Where do videos get uploaded?

**A:** To your Google Drive in the language-specific video folder. See [Google Drive Auto-Upload Setup](GDRIVE_UPLOAD_SETUP.md).

### Q: What if it fails?

**A:** Check the workflow logs via "View All Workflows" button. Common issues:

- Missing files in Google Drive
- File naming mismatch
- Google Drive folder IDs not configured

### Q: Team members don't have GitHub accounts

**A:** Perfect! That's why we auto-upload to Google Drive. They access videos directly from Drive.

---

## 🛠️ Advanced: Manual GitHub Trigger

For developers or advanced users, you can trigger workflows directly on GitHub:

```
https://github.com/srisatupasi2498/image_audio_video_maker/actions/workflows/generate-videos.yml
```

1. Click **"Run workflow"**
2. Fill the form
3. Click green **"Run workflow"** button

---

## 📞 Need Help?

- **Google Drive Setup:** See [GOOGLE_DRIVE_SETUP.md](GOOGLE_DRIVE_SETUP.md)
- **Auto-Upload Setup:** See [GDRIVE_UPLOAD_SETUP.md](GDRIVE_UPLOAD_SETUP.md)
- **Technical Issues:** Check [GitHub Issues](https://github.com/srisatupasi2498/image_audio_video_maker/issues)

---

**Happy Video Generating! 🎬**

Example: For English videos, check:

```
Srisatupasi > GG ENGLISH > video files > MP4 files
```

---

## 💬 Communication with Team

When your team says: _"We uploaded GGENG001-003 images and audio"_

You:

1. Open the bookmark
2. Click "Run workflow"
3. Select: Language=ENGLISH, Start=1, End=3
4. Click green button
5. Reply: _"Started! Videos will be ready in ~20 minutes"_

**That's it!** No need to download/upload manually anymore.

- English
- Kannada
- Hindi
- Tamil
- Telugu
- Marathi

**Example:** If you uploaded English files, select "English"

---

### Step 3: Enter File Numbers

#### Start Number

This is the **first** file number you want to convert to video.

**Example:**

- If your first file is `GGENG001.jpg`, enter: **1**
- If your first file is `GGENG010.jpg`, enter: **10**

#### End Number

This is the **last** file number you want to convert to video.

**Example:**

- If your last file is `GGENG003.jpg`, enter: **3**
- If your last file is `GGENG015.jpg`, enter: **15**

---

### Step 4: Click "Generate Videos"

Click the big purple button that says **"Generate Videos"**

---

### Step 5: Wait for Confirmation

You'll see a green success message:

```
✅ Success! Video generation started for English (1-3).

⏱️ This will take approximately 15-20 minutes.

📁 Videos will appear in Google Drive when complete.
```

**That's it! You're done!**

The videos will automatically appear in Google Drive in 15-20 minutes.

---

## 📋 Complete Example

**Scenario:** You uploaded these files to Google Drive:

- Images: `GGENG001.jpg`, `GGENG002.jpg`, `GGENG003.jpg`
- Audio: `GGENG001.mp3`, `GGENG002.mp3`, `GGENG003.mp3`

**What to do:**

1. Open: https://vinaykumarbu.github.io/image_audio_video_maker/
2. Select Language: **English**
3. Start Number: **1**
4. End Number: **3**
5. Click **"Generate Videos"**
6. Wait 15-20 minutes
7. Check Google Drive folder for videos!

---

## ❓ Common Questions

### Q: How long does it take?

**A:** Usually 15-20 minutes for 1-3 videos. Larger batches may take longer.

### Q: Where do the videos appear?

**A:** In the same Google Drive folder structure, in a "Generated Videos" folder.

### Q: Can I generate videos for multiple languages at once?

**A:** Yes! Open the page in different browser tabs and submit one for each language.

### Q: What if I make a mistake?

**A:** Just fill the form again with the correct numbers and click generate.

### Q: How do I know if it's working?

**A:** You'll see a green success message. After 15-20 minutes, check Google Drive.

### Q: What if I don't see the success message?

**A:** Try again or contact the administrator.

---

## 🚨 Important Notes

### ✅ DO:

- Make sure image AND audio files are uploaded before generating
- Use the correct file numbers
- Wait for the success message before closing the page

### ❌ DON'T:

- Don't click "Generate Videos" multiple times (wait for the message)
- Don't close your browser immediately after clicking
- Don't use file names, only use numbers (1, 2, 3, not GGENG001)

---

## 🎯 Quick Reference Card

**Print this and keep it handy:**

```
┌─────────────────────────────────────┐
│  VIDEO GENERATOR - QUICK GUIDE      │
├─────────────────────────────────────┤
│                                     │
│ 1. Open Browser                     │
│    vinaykumarbu.github.io/          │
│    image_audio_video_maker          │
│                                     │
│ 2. Fill Form:                       │
│    ✓ Language (English, Hindi...)   │
│    ✓ Start Number (e.g., 1)         │
│    ✓ End Number (e.g., 3)           │
│                                     │
│ 3. Click "Generate Videos"          │
│                                     │
│ 4. Wait 15-20 minutes              │
│                                     │
│ 5. Check Google Drive               │
│                                     │
│ Need Help? Contact: [Your Contact] │
│                                     │
└─────────────────────────────────────┘
```

---

## 📞 Support

If you have any issues:

1. Take a screenshot of the error message
2. Note down what numbers you entered
3. Contact: **[Add your contact info here]**

---

**Remember:** You're just 3 clicks away from automated video generation! 🎬
