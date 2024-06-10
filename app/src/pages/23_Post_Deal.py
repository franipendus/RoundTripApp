import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests

SideBarLinks()

# allows a user to post a deal
st.write("### Post a deal:")

admin = st.session_state['id']

date = st.date_input('Date of Deal',                  
                    label_visibility="visible")

deal_name = st.text_input('Deal Name',           
                    label_visibility="visible")
    
description = st.text_area('Deal Description',           
                    label_visibility="visible")

city = st.selectbox('Deal City', 
                       ('Rome', 'Mardid', 'London', 'Paris'),                  
                    label_visibility="visible")

hotel_name = st.selectbox('Hotel Name', 
                       ('Hyatt', 'Hilton', 'Marriott', 'Four Seasons'),                  
                    label_visibility="visible")

hotel_id_options = requests.get(f'http://api:4000/d/hotelids/{hotel_name}/{city}').json()

hotel_list_ids = []

for i in hotel_id_options:
    hotel_list_ids.append(int(i['Hotel ID'])) 


hotel_id = st.selectbox('Hotel ID', 
                       hotel_list_ids,                  
                    label_visibility="visible")

info = {'date': date.strftime('%Y-%m-%d'), 
        'hotel_id' : hotel_id, 
        'description': description, 
        'city' : city, 
        'admin' : admin,
        'hotel_name' : hotel_name,
        'deal_name': deal_name}
url = f'http://api:4000/d/post'

if st.button('Submit', type = 'primary', use_container_width=True):
    res = requests.post(url, json = info)
    if res.status_code == requests.codes.ok:
        st.write('Deal added!')
    print(res.text)

# allows the user to return to the deal admin home page 
if st.button('Return home'):
    st.switch_page('pages/20_Deal_Administrator_Home.py')