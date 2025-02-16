import streamlit as st
from meta_ai_api import MetaAI

def get_weather(place):
    llm = MetaAI()
    instruction = f'''
    you are a custom weather bot. You need to provide the weather information of given place 
    in proper format. Format the response like this:
    
    🌍 Location: [city, country]
    🌡️ Temperature: [temp]°C
    💨 Wind: [speed] km/h
    💧 Humidity: [percentage]%
    ⛅ Conditions: [weather conditions]
    
    - the given place is {place}
    if user input something else then you have to tell us that you are weather bot and you can only provide weather information
    '''
    response = llm.prompt(instruction)
    return response["message"]

def main():
    # Set page config
    st.set_page_config(page_title="Weather Bot", page_icon="🌤️")
    
    # Custom CSS for better formatting
    st.markdown("""
        <style>
        .weather-info {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f0f2f6;
            padding: 10px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Weather Information Bot 🌤️")
    st.write("Enter a city name to get weather information")
    
    # User input
    place = st.text_input("Enter the place (i.e city with country):")
    
    if st.button("Get Weather"):
        if place:
            with st.spinner("Fetching weather information..."):
                weather_info = get_weather(place)
                st.markdown(f'<div class="weather-info">{weather_info}</div>', unsafe_allow_html=True)
        else:
            st.warning("Please enter a place name")
    
    # Footer
    st.markdown(
        '<div class="footer">Made with ❤️ by Shaheer Ahmad</div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main() 