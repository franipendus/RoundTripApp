import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# provides a quick blurb about the app (RoundTrip)
st.write("# About this App")

st.markdown (
    """
    Streamline your travel planning with our all-in-one app. 
    View or update your trips, find the best times to travel, stay updated with travel advisories, and access exclusive  hotel deals.
    Advertisers can purchase ad space, gain insights into ad performance, and reach a wide audience. 
    Deal Administrators can post hotel deals and view the attraction their promotions are receiving. 
    Simplify your travel plans and marketing efforts with our practical and user-friendly app.
    Stay tuned for more information and features to come!
    """
    )

if st.button('Return home'):
    st.switch_page('Home.py')
