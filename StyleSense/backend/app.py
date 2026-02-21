import streamlit as st
import os
from groq import Groq
from datetime import datetime
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set page config
st.set_page_config(
    page_title="StyleSense - AI Fashion Recommendations",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        border-left: 4px solid #e74c3c;
    }
    .recommendation-card {
        background-color: #ecf0f1;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #3498db;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Groq client
def init_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("⚠️ GROQ_API_KEY environment variable not set!")
        st.info("Please set your Groq API key as an environment variable.")
        st.stop()
    return Groq(api_key=api_key)

# Load prompt templates
def load_prompts():
    return {
        "outfit_recommendation": """You are a professional fashion stylist AI. Based on the following user preferences, generate 3 personalized outfit recommendations with specific clothing pieces, colors, and styling tips.

User Profile:
- Body Type: {body_type}
- Style Preference: {style_preference}
- Color Preference: {color_preference}
- Budget: {budget}
- Occasion: {occasion}

Please provide:
1. Three complete outfit recommendations
2. Specific clothing items with colors
3. Styling tips for each outfit
4. Why each outfit works for this person

Format the response clearly with outfit numbers and detailed descriptions.""",

        "trend_analysis": """You are a fashion trend analyst. Analyze current fashion trends for {season} {year} and provide recommendations for someone with the following profile:
- Style: {style_preference}
- Color Preference: {color_preference}
- Body Type: {body_type}

Provide:
1. Top 3 trending items to invest in
2. Color trends they should consider
3. How to incorporate trends into their personal style
4. Timeless pieces that complement trends""",

        "styling_guide": """You are an expert fashion consultant. Create a comprehensive styling guide for someone with the following characteristics:
- Body Type: {body_type}
- Style: {style_preference}
- Color Preference: {color_preference}

Include:
1. Best cut and fit recommendations
2. Proportioning rules
3. Color combinations that work best
4. Accessories recommendations
5. Common styling mistakes to avoid"""
    }

@st.cache_resource
def get_groq_client():
    return init_groq_client()

def generate_recommendation(client, prompt, **kwargs):
    formatted_prompt = prompt.format(**kwargs)
    
    try:
        with st.spinner("🤖 StyleSense is analyzing your fashion profile..."):
            message = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": formatted_prompt}],
                max_tokens=2048,
                temperature=0.7
            )
        return message.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating recommendation: {str(e)}")
        return None

# Main App
def main():
    st.markdown("<h1 class='main-header'>👗 StyleSense</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #7f8c8d;'>AI-Powered Fashion Recommendation System</p>", 
                unsafe_allow_html=True)
    
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio(
        "Choose a feature:",
        ["Home", "Outfit Recommendations", "Trend Analysis", "Styling Guide", "About"]
    )
    
    # Initialize prompts and client
    prompts = load_prompts()
    
    if app_mode == "Home":
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Welcome to StyleSense! 👋
            
            Your personal AI fashion stylist powered by advanced generative AI.
            
            **Features:**
            - 🎨 **Outfit Recommendations** - Get personalized outfit suggestions
            - 📊 **Trend Analysis** - Discover current fashion trends
            - 👔 **Styling Guide** - Learn styling principles for your body type
            - 🎯 **AI-Powered** - Using LLaMA 3.3 70B model for intelligent insights
            """)
        
        with col2:
            st.markdown("""
            ### Get Started! 🚀
            
            1. **Select a feature** from the sidebar
            2. **Fill in your preferences** (body type, style, colors)
            3. **Get instant recommendations** powered by AI
            4. **Apply the tips** to your wardrobe
            
            No more wardrobe stress - let AI help you look your best!
            """)
        
        st.divider()
        st.markdown("""
        ### Why StyleSense?
        - 📱 Personalized to YOUR body type and preferences
        - 🎯 Trend-aware recommendations
        - 💡 Expert styling principles explained
        - ⚡ Instant results powered by Groq AI
        """)
    
    elif app_mode == "Outfit Recommendations":
        st.header("🎨 Outfit Recommendations")
        st.write("Get personalized outfit suggestions based on your preferences")
        
        col1, col2 = st.columns(2)
        
        with col1:
            body_type = st.selectbox(
                "Body Type:",
                ["Pear", "Apple", "Hourglass", "Rectangle", "Inverted Triangle"]
            )
            style_preference = st.selectbox(
                "Style Preference:",
                ["Casual", "Formal", "Bohemian", "Minimalist", "Streetwear", "Vintage", "Preppy"]
            )
        
        with col2:
            color_preference = st.multiselect(
                "Favorite Colors:",
                ["Black", "White", "Navy", "Earth Tones", "Pastels", "Bright Colors", "Neutrals"],
                default=["Black", "White"]
            )
            budget = st.selectbox(
                "Budget Range:",
                ["Budget-Friendly", "Mid-Range", "Premium", "Luxury"]
            )
        
        occasion = st.selectbox(
            "Occasion:",
            ["Casual Daily Wear", "Office/Work", "Date Night", "Party", "Weekend", "Gym/Active"]
        )
        
        if st.button("Generate Outfit Recommendations", key="outfit_btn"):
            client = get_groq_client()
            recommendation = generate_recommendation(
                client,
                prompts["outfit_recommendation"],
                body_type=body_type,
                style_preference=style_preference,
                color_preference=", ".join(color_preference),
                budget=budget,
                occasion=occasion
            )
            
            if recommendation:
                st.markdown("<div class='recommendation-card'>", unsafe_allow_html=True)
                st.markdown(recommendation)
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Save to history
                if "history" not in st.session_state:
                    st.session_state.history = []
                st.session_state.history.append({
                    "type": "outfit",
                    "timestamp": datetime.now().isoformat(),
                    "data": recommendation
                })
    
    elif app_mode == "Trend Analysis":
        st.header("📊 Fashion Trend Analysis")
        st.write("Discover current trends tailored to your style")
        
        col1, col2 = st.columns(2)
        
        with col1:
            style_preference = st.selectbox(
                "Your Style:",
                ["Casual", "Formal", "Bohemian", "Minimalist", "Streetwear", "Vintage", "Preppy"],
                key="trend_style"
            )
            season = st.selectbox(
                "Season:",
                ["Spring", "Summer", "Fall", "Winter"]
            )
        
        with col2:
            color_preference = st.multiselect(
                "Color Preferences:",
                ["Black", "White", "Navy", "Earth Tones", "Pastels", "Bright Colors", "Neutrals"],
                default=["Black", "White"],
                key="trend_colors"
            )
            body_type = st.selectbox(
                "Body Type:",
                ["Pear", "Apple", "Hourglass", "Rectangle", "Inverted Triangle"],
                key="trend_body"
            )
        
        year = datetime.now().year
        
        if st.button("Analyze Trends", key="trend_btn"):
            client = get_groq_client()
            recommendation = generate_recommendation(
                client,
                prompts["trend_analysis"],
                season=season,
                year=year,
                style_preference=style_preference,
                color_preference=", ".join(color_preference),
                body_type=body_type
            )
            
            if recommendation:
                st.markdown("<div class='recommendation-card'>", unsafe_allow_html=True)
                st.markdown(recommendation)
                st.markdown("</div>", unsafe_allow_html=True)
    
    elif app_mode == "Styling Guide":
        st.header("👔 Styling Guide")
        st.write("Learn expert styling principles for your body type and preferences")
        
        col1, col2 = st.columns(2)
        
        with col1:
            body_type = st.selectbox(
                "Select Your Body Type:",
                ["Pear", "Apple", "Hourglass", "Rectangle", "Inverted Triangle"],
                key="guide_body"
            )
            style_preference = st.selectbox(
                "Style Preference:",
                ["Casual", "Formal", "Bohemian", "Minimalist", "Streetwear", "Vintage", "Preppy"],
                key="guide_style"
            )
        
        with col2:
            color_preference = st.multiselect(
                "Color Preferences:",
                ["Black", "White", "Navy", "Earth Tones", "Pastels", "Bright Colors", "Neutrals"],
                default=["Black", "White"],
                key="guide_colors"
            )
        
        if st.button("Get Styling Guide", key="guide_btn"):
            client = get_groq_client()
            recommendation = generate_recommendation(
                client,
                prompts["styling_guide"],
                body_type=body_type,
                style_preference=style_preference,
                color_preference=", ".join(color_preference)
            )
            
            if recommendation:
                st.markdown("<div class='recommendation-card'>", unsafe_allow_html=True)
                st.markdown(recommendation)
                st.markdown("</div>", unsafe_allow_html=True)
    
    elif app_mode == "About":
        st.header("About StyleSense")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🎯 What is StyleSense?
            
            StyleSense is an AI-powered fashion recommendation system that uses advanced generative AI 
            to provide personalized fashion advice. Our system understands your body type, style preferences, 
            and color palettes to suggest outfits and styling tips that work best for you.
            
            ### 🔧 Technology Stack
            - **Streamlit** - Web application framework
            - **Groq** - Fast AI inference
            - **LLaMA 3.3 70B** - Advanced language model
            - **Python** - Backend logic
            """)
        
        with col2:
            st.markdown("""
            ### 🌟 Features
            - Personalized outfit recommendations
            - Trend analysis based on season
            - Styling guides by body type
            - Budget-conscious suggestions
            - Occasion-specific recommendations
            
            ### 📧 Built with ❤️
            Fashion meets AI technology to help you express your style confidently!
            """)

if __name__ == "__main__":
    main()
