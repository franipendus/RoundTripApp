import logging
logger = logging.getLogger()
import streamlit as st
import requests


import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')
logger.info('In the broken function')
# Show appropriate sidebar links for the role of the currently logged in user

# welcome for a sys admin 
st.title(f"Welcome System Administrator.")
st.write('')
st.write('')

# allows admin to pick an ml model and train it
st.write("### Train an ML Model:")
if st.button('Model 1'):
    pre_results = requests.get(f'http://api:4000/p/ml_models/1')
    logger.info(f'res = {pre_results}')
    if pre_results.status_code == 200:
        st.write('Model 1 trained: success :)')
    else:
        st.write('Model 1 trained: failed :(')

if st.button('Model 2'):
    pre_results = requests.get(f'http://api:4000/p/ml_models/2')
    logger.info(f'res = {pre_results}')
    if pre_results.status_code == 200:
        st.write('Model 2 trained: success :)')
    else:
        st.write('Model 2 trained: failed :(')

# allows the sys admin to logout and go to the home page
if st.button("Logout"):
        st.switch_page('Home.py')
