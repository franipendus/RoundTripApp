import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

# creates the front-end page for ad impressions 
st.title('Ad Impressions')

# allows a user to selected an ad and view its impressions 
st.write("### Select an ad to view impressions:")
id = st.session_state['id']
options = requests.get(f'http://api:4000/a/advertisers/adids/{id}').json()

ids = []

for i in options:
    ids.append(int(i['Ad ID'])) 


num = st.selectbox('Ad ID', 
                       ids,                  
                    label_visibility="visible")

results = requests.get(f'http://api:4000/a/advertisers/adimp/{id}/{num}').json()
st.table(results)

# allows a user to see which travelers interacted with their ads 
st.write("### Want the information about the impressions from a specific traveler?")
num = st.number_input('Traveler ID', min_value=1, max_value=50, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/a/advertisers/adimp/trav/{id}/{num}').json()
st.table(results)

