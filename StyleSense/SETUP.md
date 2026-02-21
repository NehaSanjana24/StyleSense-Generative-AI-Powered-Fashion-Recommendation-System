# StyleSense Setup Instructions

## Quick Start Guide

### 1. Install Dependencies
```powershell
cd c:\Users\mopar\OneDrive\Desktop\StyleSense
pip install -r requirements.txt
```

### 2. Configure Your Groq API Key

Replace `your_groq_api_key_here` with your actual API key from Groq.

**Option A: Using .env file (Recommended)**
- Create a file named `.env` in the StyleSense root directory
- Add: `GROQ_API_KEY=your_actual_api_key`

**Option B: Using Environment Variable (PowerShell)**
```powershell
$env:GROQ_API_KEY="your_actual_api_key"
```

**Option C: Using Environment Variable (Persistent)**
1. Press `Win + X` → System
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Under "User variables", click "New"
5. Variable name: `GROQ_API_KEY`
6. Variable value: Your API key
7. Click OK and restart PowerShell

### 3. Get Your Groq API Key
1. Go to https://console.groq.com
2. Sign up or log in
3. Click "API Keys" in the left sidebar
4. Create a new API key
5. Copy the key (you'll see it only once!)
6. Add it to your .env file or environment variable

### 4. Run the Application
```powershell
streamlit run backend/app.py
```

This will automatically open your browser at `http://localhost:8501`

### 5. Start Using StyleSense!
- Choose a feature from the sidebar
- Fill in your preferences
- Click the button to get AI-powered recommendations
- Enjoy personalized fashion advice!

## Verifying the Setup

To verify your Groq API key is correctly set:

```powershell
# In PowerShell, you can check by running:
$env:GROQ_API_KEY

# It should return your API key, not blank
```

## Features Overview

### 🎨 Outfit Recommendations
- Get 3 personalized outfit suggestions
- Based on body type, style, colors, budget, and occasion
- Includes styling tips for each outfit

### 📊 Trend Analysis
- Discover trending items for the season
- See color trends relevant to you
- Learn how to incorporate trends into your style

### 👔 Styling Guide
- Expert styling principles for your body type
- Color combination recommendations
- Common styling mistakes to avoid

## Troubleshooting

**Q: "GROQ_API_KEY environment variable not set!"**
- A: Make sure your API key is properly configured in .env or environment variables
- Restart the Streamlit app after setting the key

**Q: "Error generating recommendation"**
- A: Check your internet connection and API key validity

**Q: "Module not found" error**
- A: Run `pip install -r requirements.txt` again

---

You're all set! Enjoy StyleSense! 🎉
