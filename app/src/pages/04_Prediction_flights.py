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

st.write('### Flight Prediction with Regression')

# create a 2 column layout
col1, col2, col3, col4, col5 = st.columns(5)

# add one number input for variable 1 into column 1 flight price
with col1:
  var_012 = st.number_input('Hotel Price:',  min_value=0.0)

# add another number input for variable 2 into column 2 hotel rating
with col2:
  var_022 = st.number_input('Hotel Rating:',  min_value=1, max_value=5, value= 1, 
                           step=1)
  
# add another number input for variable 3 into column 3 origin city
with col3:
  var_032 = st.selectbox('Origin City:', ('London', 'Madrid', 'Rome', 'Paris'))
  
# add another number input for variable 4 into column 4 destination city
with col4:
  var_042 = st.selectbox('Destination City:', ('London', 'Madrid', 'Rome', 'Paris'))

# add another number input for variable 5 into column 5 month
with col5:
  var_052 = st.selectbox('In which month do you want to travel?:', ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))


logger.info(f'var_01 = {var_012}')
logger.info(f'var_02 = {var_022}')

# add a button to use the values entered into the number field to send to the 
# prediction function via the REST API
if st.button('Calculate Prediction',
             type='primary',
             use_container_width=True):

  # submitting the query to get the prediction
  query = f'http://api:4000/p/ml_models/2/{var_012}/{var_022}/{var_032}/{var_042}/{var_052}'
  
  # converting the query result to a rounded float
  results2 = requests.get(query).json()
  cost2 = float(results2["result"]).__round__(2)
  
  # display the result from the query 
  st.write('### Predicted Flight cost (one-way):')
  st.metric("US $$$", str(cost2), delta=None, delta_color="normal", help=None, label_visibility="visible")





  



  