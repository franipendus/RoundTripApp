import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.title('Ad Impressions')

st.write("### Your ads:")
num = st.number_input('Ad ID', min_value=1, max_value=10, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/a/advertisers/adimp/{num}').json()
st.table(results)

st.write("### Want the information about a specific traveler's impressions?")
num = st.number_input('Traveler ID', min_value=1, max_value=50, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/a/advertisers/adimp/trav/{num}').json()
st.table(results)

