import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import requests
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Trips')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")




# add a button to use the values entered into the number field to send to the 
# prediction function via the REST API
st.write("### Your trips:")
num = st.number_input('Traveler ID', min_value=1, max_value=50, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/t/travelers/trips/{num}').json()
st.dataframe(results)


st.write("### Your Favorite Hotels:")
city = st.selectbox('City', 
                       options= ('Paris', 'Rome', 'London', 'Madrid'),                  
                    label_visibility="visible")

results = requests.get(f'http://api:4000/t/travelers/favhotels/{city}/{num}').json()
st.table(results)

st.write("### Update a hotel booking:")
hotel_id = st.number_input('Hotel ID', min_value=1, max_value=20, value= 1,                  
                    label_visibility="visible")
sdate = st.date_input('Start Date',                  
                    label_visibility="visible")
edate = st.date_input('End Date',            
                    label_visibility="visible")

results = requests.get(f'http://api:4000/t/travelers/hotelbook/<sdate>/<edate>/<hotel_id>').json()
st.table(results)

