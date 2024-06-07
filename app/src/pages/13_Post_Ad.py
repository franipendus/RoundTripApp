import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests
import logging

logger = logging.getLogger()
SideBarLinks()

st.write("### Post an ad:")

adver_id = st.session_state['id']


date = st.date_input('Date Posted',                  
                    label_visibility="visible")
    
description = st.text_area('Ad Description',           
                    label_visibility="visible")
price = st.number_input('Price', min_value=0.0, max_value=250.0,             
                    label_visibility="visible")
title = st.text_input('Ad Title',           
                    label_visibility="visible")

info = {
    'date': date.strftime('%Y-%m-%d'),  
    'adver_id': adver_id,
    'description': description,
    'price': price,
    'title': title
}
url = f'http://api:4000/a/advertisers/adinfo'

if st.button('Submit'):
    res = requests.post(url, json=info)
    if res.status_code == requests.codes.ok:
        st.write('Ad added!')
    print(res.text)

if st.button('Return home'):
    st.switch_page('pages/10_Advertiser_Home.py')