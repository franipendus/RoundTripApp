import logging
logger = logging.getLogger()
import streamlit as st
import requests


import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')
logger.info('In the broken function')
# Show appropriate sidebar links for the role of the currently logged in user

st.title(f"Welcome System Administrator.")
st.write('')
st.write('')
st.write("### Train an ML Model:")
if st.button('Model 1'):
    pre_results = requests.get(f'http://api:4000/p/ml_models/1')
    logger.info(f'res = {pre_results}')
    #results = pre_results.json()
    st.write(pre_results)

if st.button("Home"):
        st.switch_page('Home.py')
