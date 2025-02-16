import streamlit as st
from meta_ai_api import MetaAI

# Page configuration
st.set_page_config(
    page_title="Weather Bot",
    page_icon="🌤️",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #1E88E5;
        font-size: 3rem !important;
        padding-bottom: 2rem;
        text-align: center;
    }
    .stTextInput > label {
        font-size: 1.2rem;
        color: #424242;
        font-weight: 500;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 1rem;
        font-size: 1.1rem;
    }
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        background-color: #1E88E5;
        color: white;
        font-size: 1.1rem;
        padding: 0.5rem 1rem;
        margin-top: 1rem;
    }
    .weather-box {
        padding: 25px;
        border-radius: 15px;
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e9f2 100%);
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        font-size: 1.1rem;
        line-height: 2;
    }
    .description {
        text-align: center;
        color: #616161;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .stSpinner > div {
        text-align: center;
        color: #1E88E5;
    }
    .stWarning {
        padding: 1rem;
        border-radius: 10px;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("Weather Information Bot")
    st.markdown('<p class="description">Get instant weather updates for any location worldwide! 🌍</p>', unsafe_allow_html=True)
    
    # Create two columns for layout
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Initialize MetaAI
        llm = MetaAI()
        
        # Create input field
        place = st.text_input("Enter the place (i.e city with country):")
    
    with col2:
        st.write("")
        st.write("")
        search_button = st.button("🔍 Search")
    
    if search_button:
        if place:
            instruction = f'''
            You are a weather information bot. Provide weather information for {place} in the following format:
            
            🌍 Location: [city, country]
            🌡️ Temperature: [temperature in °C]
            💨 Wind: [wind speed and direction]
            💧 Humidity: [humidity percentage]
            ☁️ Weather Condition: [current weather condition]
            🌅 Sunrise: [sunrise time]
            🌇 Sunset: [sunset time]
            
            Provide only these details in this exact format with emojis. If location is invalid, politely mention that you can only provide weather information for valid locations.
            '''
            
            with st.spinner("Fetching weather information..."):
                response = llm.prompt(instruction)
                st.markdown(f'<div class="weather-box">{response["message"]}</div>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter a place name")

    # Footer
    st.markdown("""
        <div style='position: fixed; bottom: 0; left: 0; width: 100%; background-color: #f0f2f6; padding: 10px; text-align: center;'>
            <p style='color: #616161; margin: 0;'>Made with ❤️ by Shaheer Ahmad</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()