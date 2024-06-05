import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title(f"Welcome Deal Administrator, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write("### About")
st.write("As a Deal Administrator, you can:")

st.markdown("- view your deals")
st.markdown("- view deal impressions")
st.markdown("- post/delete a deal")
  
st.write('#### Use the side bar to chose what you would like to do today')