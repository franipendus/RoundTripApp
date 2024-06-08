import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

# allows user to see deal impressions 
st.title('Deal Impressions')

# shows user the impressions for their posted deals 
st.write("### Your deal impressions:")
id = st.session_state['id']
results = requests.get(f'http://api:4000/d/dealadmin/dealimps/{id}').json()
st.table(results)

# shows impressions for the user's posted deal broken down by traveler
st.write("### Want the information about a specific traveler's impressions?")
num = st.number_input('Traveler ID', min_value=1, max_value=50, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/d/dealadmin/dealimps/trav/{id}/{num}').json()
st.table(results)

