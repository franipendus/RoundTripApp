import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# welcome for a traveler 
st.title(f"Welcome Traveler, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write("### About")
st.write("As a traveler, you can:")


# lists what the traveler can do 
st.markdown(f"- view/update a trip") 
st.markdown(f"- view country information")
st.markdown(f"- view hotel promotions")
st.markdown(f"- view hotel and flight cost predictions")

# creates buttons and allows user to pick a page 
st.write('#### What you would like to do today?')
if st.button('Trips ✈️'):
    st.switch_page('pages/01_Trips.py')
if st.button('Country Information 🗺️'):
    st.switch_page('pages/02_Countries.py')
if st.button('Hotel Promotions 💲'):
    st.switch_page('pages/03_Promotions.py')
if st.button('Flight Predictions'):
    st.switch_page('pages/04_Prediction_flights.py')
if st.button('Hotel Predictions'):
    st.switch_page('pages/04_Prediction_hotels.py')


