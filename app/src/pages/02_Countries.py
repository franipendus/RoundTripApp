import streamlit as st
from streamlit_extras.app_logo import add_logo
import pandas as pd
import pydeck as pdk
import requests
from streamlit_folium import st_folium 
import folium
from urllib.error import URLError
from modules.nav import SideBarLinks

SideBarLinks()

# add the logo
add_logo("assets/logo.png", height=400)

# set up the page
st.markdown("# Country Info")
st.sidebar.header("Country Info")


st.write("Select a country from the dropdown below to find out more")


country = st.selectbox('Country', 
                       options= ('France', 'Italy', 'United Kingdom', 'Spain'),
                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/t/travelers/countries/{country}').json()
st.table(results)


loc = (0.0, 0.0)
lm = (0.0,0.0)
str = ''
cap = ''
lang = ''

if country == 'France':
    loc = (48.8575, 2.3514)
    lm = (48.8584, 2.2945)
    str = 'Eiffel Tower'
    cap = 'Paris'
    lang = 'Bienvenue à Paris, France'
if country == 'Spain':
     loc = (40.4168, -3.7038)
     lm = (40.418407, -3.712354)
     str = 'Plaza de Oriente'
     cap = 'Mardid'
     lang = 'Bienvenido a madrid, españa'
if country == 'United Kingdom':
     loc = (51.5072, -0.1276)
     lm = (51.5007, -0.1246)
     str = 'Big Ben'
     cap = 'London'
if country == 'Italy':
     loc = (41.8967, 12.4822)
     lm = (41.8902, 12.4922)
     str = 'Colosseum'
     cap = 'Rome'
     lang = 'Bienvenue à Rome, Italie'

m = folium.Map(location = loc, zoom_start = 16)

folium.Marker(lm, popup = str, tooltip = str).add_to(m)         
folium.Marker(loc, popup = cap, tooltip = cap).add_to(m)   

st.write(f'### Welcome to {cap}, {country}!')
st.write(f'#### {lang}!')

st_data = st_folium(m, width = 750)
