import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Deal Information')

st.write("### Your deals:")
id = st.session_state['id']
results = requests.get(f'http://api:4000/d/dealadmin/deals/{id}').json()
st.table(results)


st.write("### Want the deal information about a specific hotel?")
options = requests.get(f'http://api:4000/d/hotelids/{id}').json()

ids = []

for i in options:
    ids.append(int(i['Hotel ID'])) 


hotel = st.selectbox('Hotel ID', 
                       ids,                  
                    label_visibility="visible")

results = requests.get(f'http://api:4000/d/dealadmin/dealinfospecific/{id}/{hotel}').json()
st.table(results)