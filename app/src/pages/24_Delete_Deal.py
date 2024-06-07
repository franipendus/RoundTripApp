import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.write("### Delete a Deal:")
admin = st.session_state['id']

options = requests.get(f'http://api:4000/d/dealids/{admin}').json()

ids = []

for i in options:
    ids.append(int(i['Deal ID'])) 


deal_id = st.selectbox('Deal ID', 
                       ids,                  
                    label_visibility="visible")

if st.button("Delete", 
            type='primary', 
            use_container_width=True):
    url = f'http://api:4000/d/deals/del/{deal_id}'
    response = requests.delete(url)
    
    if response.status_code == 200 or response.status_code == 204:
        st.write('Deal deleted successfully!')
    else:
        st.write(f'Delete failed :( {response.status_code}')

if st.button('Return home'):
    st.switch_page('pages/20_Deal_Administrator_Home.py')