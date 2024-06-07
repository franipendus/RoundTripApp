import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.title('Ad Impressions')

st.write("### Select an ad to view impressions:")
id = st.session_state['id']
num = st.number_input('Ad ID', min_value=1, max_value=10, value= 1,                  
                    label_visibility="visible")

results = requests.get(f'http://api:4000/a/advertisers/adimp/{id}/{num}').json()
st.table(results)

st.write("### Want the information about the impressions from a specific traveler?")
num = st.number_input('Traveler ID', min_value=1, max_value=50, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/a//advertisers/adimp/trav/{id}/{num}').json()
st.table(results)

