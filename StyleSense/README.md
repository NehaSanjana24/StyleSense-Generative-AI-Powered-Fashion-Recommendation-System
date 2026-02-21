# StyleSense - AI-Powered Fashion Recommendation System

A generative AI platform that provides personalized fashion recommendations, styling guidance, and trend-based insights using Groq's LLaMA 3.3 model.

## 🎯 Features

- **👗 Outfit Recommendations** - Get personalized outfit suggestions based on body type, style preference, colors, and occasion
- **📊 Trend Analysis** - Discover current fashion trends tailored to your preferences
- **👔 Styling Guide** - Learn expert styling principles for your body type
- **🎨 Color Matching** - Get intelligent color combination suggestions
- **⚡ Fast AI Processing** - Powered by Groq's ultra-fast LLaMA 3.3 70B model

## 📋 Tech Stack

- **Frontend/UI**: Streamlit
- **AI Engine**: Groq + LLaMA 3.3 70B
- **Language**: Python 3.8+
- **Dependencies**: See `requirements.txt`

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Groq API Key (get it from [console.groq.com](https://console.groq.com))

### Step 1: Clone/Setup the Project
```bash
cd c:\Users\mopar\OneDrive\Desktop\StyleSense
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

Or set the environment variable on your system:
**Windows:**
```powershell
$env:GROQ_API_KEY="your_groq_api_key_here"
```

### Step 4: Run the Application
```bash
streamlit run backend/app.py
```

The app will open at `http://localhost:8501`

## 📱 Usage

1. **Home Page** - Introduction and feature overview
2. **Outfit Recommendations**
   - Select your body type
   - Choose style preferences
   - Pick favorite colors
   - Set budget range
   - Choose occasion
   - Get AI-powered recommendations

3. **Trend Analysis**
   - Select your style and colors
   - Choose the season
   - Get trend insights personalized to you

4. **Styling Guide**
   - Learn styling principles for your body type
   - Get color combination tips
   - Understand fashion rules that work for you

## 🎨 Customization

### Adding New Styles
Edit the selectbox options in `backend/app.py` to add more style preferences, body types, or occasions.

### Adjusting Prompts
The AI prompts are defined in the `load_prompts()` function. Modify them to change recommendation styles or add new features.

### UI Customization
The CSS styling is in the `st.markdown()` call. Customize colors, fonts, and layouts to match your brand.

## 📊 Project Structure

```
StyleSense/
├── backend/
│   └── app.py                 # Main Streamlit application
├── frontend/                  # Optional: Custom HTML/CSS/JS UI
├── models/                    # Prompt templates and configurations
├── assets/                    # Images and resources
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
└── README.md                 # This file
```

## 🔑 API Key Setup

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up or log in
3. Create an API key
4. Add it to your `.env` file or system environment variables
5. Start using StyleSense!

## 🤖 AI Models Used

- **Model**: LLaMA 3.3 70B Versatile
- **Provider**: Groq
- **Capabilities**: Ultra-fast inference, high-quality recommendations

## 🐛 Troubleshooting

### "GROQ_API_KEY not set"
Make sure you've added your API key to the `.env` file or set it as an environment variable.

### Slow responses
Groq provides ultra-fast inference. If you experience delays, check your internet connection and API key validity.

### Import errors
Run `pip install -r requirements.txt` to ensure all dependencies are installed.

## 📄 License

This project is open source and available for educational and commercial use.

## 🤝 Contributing

Feel free to fork, modify, and enhance StyleSense! Some ideas:
- Image upload for outfit visualization
- User preference saving
- Integration with fashion APIs
- Mobile app version
- Database for tracking user preferences

---

**Built with ❤️ using Streamlit, Groq, and LLaMA**
