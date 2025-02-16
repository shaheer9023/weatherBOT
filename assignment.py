import streamlit as st
from meta_ai_api import MetaAI
from datetime import datetime
import pytz

def get_weather(place):
    llm = MetaAI()
    # Get Pakistan time
    pk_timezone = pytz.timezone('Asia/Karachi')
    current_time = datetime.now(pk_timezone).strftime('%I:%M %p, %d %B %Y')
    
    instruction = f'''
    you are a custom weather bot. You need to provide the weather information of given place 
    in proper format.
    - Format the response beautifully with emojis
    - Include temperature, humidity, and general weather conditions
    - Do not include any HTML tags in your response
    - Just provide clean text with emojis
    - Current Pakistan Time: {current_time}
    - the given place is {place}
    if user input something else then you have to tell us that you are weather bot and you can only provide weather information
    '''
    response = llm.prompt(instruction)
    return response["message"]

def main():
    st.set_page_config(page_title="Weather Bot", page_icon="🌤️")
    
    # Custom CSS for lighter background
    st.markdown("""
        <style>
        .weather-container {
            background-color: #F7FBFF;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #E1F0FF;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header styling
    st.markdown("""
        <h1 style='text-align: center; color: #2E86C1;'>☀️ Weather Information Bot 🌦️</h1>
    """, unsafe_allow_html=True)
    
    # Input section
    place = st.text_input("Enter the place (i.e city with country):", placeholder="e.g., Lahore, Pakistan")
    
    if st.button("Get Weather 🔍"):
        if place:
            with st.spinner("Fetching weather information..."):
                weather_info = get_weather(place)
                st.markdown("<div class='weather-container'>", unsafe_allow_html=True)
                st.write(weather_info)
                st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter a place name!")
    
    # Footer
    st.markdown("""
        <div style='position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px; background-color: #F8F9F9;'>
            <p style='color: #566573;'>Made with ❤️ by Shaheer Ahmad</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()