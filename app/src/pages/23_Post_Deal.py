import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests

st.write("### Post a deal:")

adver_id = st.selectbox('Advertiser Id', 
                       options= (1, 2, 3, 4, 5),                  
                    label_visibility="visible")
date = st.date_input('Date Posted',                  
                    label_visibility="visible")
    
description = st.text_area('Ad Description',           
                    label_visibility="visible")
price = st.number_input('Price', min_value=0.0, max_value=250.0,             
                    label_visibility="visible")
title = st.text_input('Ad Title',           
                    label_visibility="visible")

info = {'date': date, 
        'adver_id' : adver_id, 
        'description': description, 
        'price' : price, 
        'title' : title}
url = f'http://api:4000/a/advertisers/adinfo'

if st.button('Submit'):
    res = requests.post(url, data = info)
    if res.status_code == requests.codes.ok:
        st.write('Ad added!')
    print(res.text)

if st.button('Return home'):
    st.switch_page('pages/10_Advertiser_Home.py')