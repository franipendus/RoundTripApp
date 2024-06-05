import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Advertiser, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write("### About")
st.write("As an advertiser, you can:")

st.markdown("- view your ads")
st.markdown("- view ad impressions")
st.markdown("- post/delete an ad")
  
st.write('#### Use the side bar to chose what you would like to do today')