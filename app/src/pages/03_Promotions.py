import streamlit as st
from streamlit_extras.app_logo import add_logo
import numpy as np
import random
import time
import requests
from modules.nav import SideBarLinks

SideBarLinks()

# allows a user to see hotel promotions in a specific city 
st.write("### Select a city from the dropdown below to learn about hotel deals")
st.image('assets/hd.png')

city = st.selectbox('City', 
                       options= ('Paris', 'Rome', 'London', 'Madrid'),
                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/t/travelers/promotions/{city}').json()
st.table(results)














# def response_generator():
#   response = random.choice (
#     [
#       "Hello there! How can I assist you today?",
#       "Hi, human!  Is there anything I can help you with?",
#       "Do you need help?",
#     ]
#   )
#   for word in response.split():
#     yield word + " "
#     time.sleep(0.05)
#-----------------------------------------------------------------------

# #st.set_page_config (page_title="Sample Chat Bot", page_icon="🤖")
# add_logo("assets/logo.png", height=400)

# st.title("Echo Bot 🤖")

# st.markdown("""
#             Currently, this chat bot only returns a random message from the following list:
#             - Hello there! How can I assist you today?
#             - Hi, human!  Is there anything I can help you with?
#             - Do you need help?
#             """
#            )


# # Initialize chat history
# if "messages" not in st.session_state:
#   st.session_state.messages = []

# # Display chat message from history on app rerun
# for message in st.session_state.messages:
#   with st.chat_message(message["role"]):
#     st.markdown(message["content"])

# # React to user input
# if prompt := st.chat_input("What is up?"):
#   # Display user message in chat message container
#   with st.chat_message("user"):
#     st.markdown(prompt)
  
#   # Add user message to chat history
#   st.session_state.messages.append({"role": "user", "content": prompt})

#   response = f"Echo: {prompt}"

#   # Display assistant response in chat message container
#   with st.chat_message("assistant"):
#     # st.markdown(response)
#     response = st.write_stream(response_generator())

#   # Add assistant response to chat history
#   st.session_state.messages.append({"role": "assistant", "content": response})

