import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Traveler, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write("### About")
st.write("As a traveler, you can:")

st.markdown("- view/update a trip ")
st.markdown("- view country information")
st.markdown("- view hotel promotions")
st.markdown("- view hotel and flight cost predictions")
  
st.write('#### Use the side bar to chose what you would like to do today')

