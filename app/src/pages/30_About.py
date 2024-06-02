import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    This app is being built as an exemplar for Northeastern University's 
    Summer 2024 Dialogue of Civilization Program titled *Data and 
    Software in International Government and Politics*.  The program is bein
    led by Dr. Mark Fontenot and Dr. Eric Gerber from the Khoury College of
    Computer Sciences.  

    The goal of this demo is to provide information on the tech stack 
    being used as well as demo some of the features of the various platforms. 

    Stay tuned for more information and features to come!
    """
        )
