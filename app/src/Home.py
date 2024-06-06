import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

st.session_state['authenticated'] = False
SideBarLinks(show_home=True)

st.title('RoundTrip')

st.write('\n\n')
st.write('## Hi! Welcome to our app!')
st.write("#### Please chose which user would you like to log in as:")

if st.button("Act as Maria, a Traveler", 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'traveler'
    st.session_state['first_name'] = 'Maria'
    st.session_state['id'] = 32
    st.switch_page('pages/00_Traveler_Home.py')

if st.button('Act as Gabriel, an Advertiser', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'advertiser'
    st.session_state['first_name'] = 'Gabriel'
    st.session_state['id'] = 5
    st.switch_page('pages/10_Advertiser_Home.py')

if st.button('Act as Elliott, a Deal Administrator', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'deal_admin'
    st.session_state['first_name'] = 'Elliott'
    st.session_state['id'] = 13
    st.switch_page('pages/20_Deal_Administrator_Home.py')

if st.button('System Admin', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.switch_page('pages/40_Sys_Admin.py')
