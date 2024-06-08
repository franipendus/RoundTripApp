import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# welcome for an advertiser 
st.title(f"Welcome Advertiser, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write("### About")
st.write("As an advertiser, you can:")

# list what an advertiser can do 
st.markdown("- view your ads")
st.markdown("- view ad impressions")
st.markdown("- post/delete an ad")
  
# creates buttons and allows user to pick a page 
st.write('#### What you would like to do today?')
if st.button('Information 📢'):
    st.switch_page('pages/11_Ad_Information.py')
if st.button('Impressions 📈'):
    st.switch_page('pages/12_Ad_Impressions.py')
if st.button('Post ➕'):
    st.switch_page('pages/13_Post_Ad.py')
if st.button('Delete ❌'):
    st.switch_page('pages/14_Delete_Ad.py')
