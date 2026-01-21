import requests
import streamlit as st
############################################################
def get_weather_data(city):
    API_KEY = "955cbe94527907ffa1f5581810bd7deb"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'en',
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            return response.json(), None
        elif response.status_code == 404:
            return None,"City not found."
        else:
            return None,"Service unavailable."

    except Exception as e:
        return None, str(e)
############################################################
def main():
    st.set_page_config(page_title="Weather Lookup Tool")
    st.title("🌤️ Global Weather Dashboard")

    city_input=st.text_input("Enter city name",placeholder="e.g., New York, Tokyo, London")

    if st.button("Search Weather") or city_input:
        if city_input:
            with st.spinner('Fetching data...'):
                data, error = get_weather_data(city_input)
            if error:
                st.error(error)
            else:
                st.success(f"Weather in {data['name']}")
                st.metric("Temperature", f"{data['main']['temp']} °C")

                lat = data['coord']['lat']
                lon = data['coord']['lon']
                with st.expander("📍 View City Location on Map"):
                    map_url = f"https://www.google.com/maps?q={lat},{lon}&hl=en&z=10&output=embed"
                    components.iframe(map_url, height=400)
        else:
            st.warning("Please enter a city name.")
############################################################
if __name__ == "__main__":
    main()
