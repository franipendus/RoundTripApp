import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks
import requests
import logging
logger = logging.getLogger()

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title('Cost Predictions')
st.write('### Prediction with Regression')

# create a 2 column layout
col1, col2, col3, col4, col5 = st.columns(5)

# add one number input for variable 1 into column 1 flight price
with col1:
  var_01 = st.number_input('Flight Price:',  min_value=0.0)

# add another number input for variable 2 into column 2 hotel rating
with col2:
  var_02 = st.number_input('Hotel Rating:',  min_value=1, max_value=5, value= 1, 
                           step=1)
  
# add another number input for variable 3 into column 3 origin city
with col3:
  var_03 = st.selectbox('Origin City:', ('London', 'Madrid', 'Rome', 'Paris'))
  
# add another number input for variable 4 into column 4 destination city
with col4:
  var_04 = st.selectbox('Destination City:', ('London', 'Madrid', 'Rome', 'Paris'))

# add another number input for variable 5 into column 5 month
with col5:
  var_05 = st.selectbox('In which month do you want to travel?:', ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))


logger.info(f'var_01 = {var_01}')
logger.info(f'var_02 = {var_02}')

# add a button to use the values entered into the number field to send to the 
# prediction function via the REST API
if st.button('Calculate Prediction',
             type='primary',
             use_container_width=True):
  query = f'http://api:4000/p/ml_models/1/{var_01}/{var_02}/{var_03}/{var_04}/{var_05}'
  logger.info(f'query = {query}')
  results = requests.get(query)
  logger.info(f'results = {results}')
  
  st.write('### Predicted hotel cost:')
  st.metric("cost per night", results.json(), delta=None, delta_color="normal", help=None, label_visibility="visible")

  #st.dataframe(results.json()) 



  