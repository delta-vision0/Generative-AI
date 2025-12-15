import streamlit as st
import json
import os
import requests

api_key = os.getenv("api_key")

url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()

st.text_input("Enter city name:")
st.write(f("Temperature:",data["main"]["temp"]))
st.write(f("Humidity:",data["main"]["humidity"]))
st.write(f("Description:",data["weather"][0]["description"]))
st.write(f("Wind Speed:",data["wind"]["speed"]))

