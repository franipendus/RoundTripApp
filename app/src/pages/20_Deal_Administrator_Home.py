import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

# welcome for a deal admin
st.title(f"Welcome Deal Administrator, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write("### About")
st.write("As a Deal Administrator, you can:")

# list what a deal admin can do 
st.markdown("- view your deals")
st.markdown("- view deal impressions")
st.markdown("- post/delete a deal")
  
# creates buttons and allows user to pick a page 
st.write('#### What you would like to do today?')
if st.button('Information 📢', type = 'primary', use_container_width=True):
    st.switch_page('pages/21_Deal_Information.py')
if st.button('Impressions 📈', type = 'primary', use_container_width=True):
    st.switch_page('pages/22_Deal_Impressions.py')
if st.button('Post ➕', type = 'primary', use_container_width=True):
    st.switch_page('pages/23_Post_Deal.py')
if st.button('Delete ❌', type = 'primary', use_container_width=True):
    st.switch_page('pages/24_Delete_Deal.py')