import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Deal Information')

# if st.button('Post a Deal'):
#     st.switch_page('pages/23_Post_Deal.py')

# if st.button('Delete an Deal'):
#     st.switch_page('pages/24_Delete_Deal.py')

st.write("### Your deals:")
num = st.number_input('Deal Administrator ID', min_value=1, max_value=50, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/d/dealadmin/deals/{num}').json()
st.table(results)


st.write("### Want the deal information about a specific hotel?")
num = st.number_input('Hotel ID', min_value=1, max_value=20, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/d/dealadmin/dealinfospecific/{num}').json()
st.table(results)