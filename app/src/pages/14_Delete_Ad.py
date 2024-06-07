import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.write("### Delete an ad:")

# help with this
adver_id = st.session_state['id']


options = requests.get(f'http://api:4000/a/advertisers/adids/{adver_id}').json()

ids = []

for i in options:
    ids.append(int(i['Ad ID'])) 


ad_id = st.selectbox('Ad ID', 
                       ids,                  
                    label_visibility="visible")

if st.button("Delete", 
            type='primary', 
            use_container_width=True):
    url = f'http://api:4000/a/advertisers/adinfo/{ad_id}'
    response = requests.delete(url)
    
    if response.status_code == 200 or response.status_code == 204:
        st.write('Ad deleted successfully!')
    else:
        st.write(f'Delete failed :( {response.status_code}')
    
if st.button('Return home'):
    st.switch_page('pages/10_Advertiser_Home.py')