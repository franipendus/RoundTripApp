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

st.write("### Update a trip:")
trip_id = st.number_input('Trip ID', min_value=1, max_value=250, value= 1,                  
                    label_visibility="visible")
sdate = st.date_input('Start Date',                  
                    label_visibility="visible")
edate = st.date_input('End Date',            
                    label_visibility="visible")

stuff = {'s': sdate.strftime('%H:%M:%D'), 'e': edate.strftime('%H:%M:%D'), 'ti' : trip_id}
if st.button("Submit", 
            type = 'primary', 
            use_container_width=True):
        results = requests.put(f'http://api:4000/t/travelers/trips', json = stuff)
        
        if results.status_code == 200 or results.status_code == 201:
                st.write('Trip updated!')
        else : st.write('Update failed :( Status Code = ' + str(results.status_code))   
            

#st.table(results)

