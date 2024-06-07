# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Examples for Role of travelers ------------------------
def TravelerHomeNav():
    st.sidebar.page_link("pages/00_Traveler_Home.py", label="Traveler Home", icon='🏠')

def TripsNav():
    st.sidebar.page_link("pages/01_Trips.py", label="Trips", icon='✈️')

def CountriesNav():
    st.sidebar.page_link("pages/02_Countries.py", label="Countries", icon='🗺️')

def PromosNav():
    st.sidebar.page_link("pages/03_Promotions.py", label="Promotions", icon='💲')

def CostPred():
    st.sidebar.page_link("pages/04_Prediction.py", label="Predictions", icon='🔮')

## ------------------------ Examples for Role of advertisers ------------------------
def AdInfoNav():
    st.sidebar.page_link("pages/11_Ad_Information.py", label="Ad Information", icon='📢')

def AdImpNav():
    st.sidebar.page_link("pages/12_Ad_Impressions.py", label="Ad Impressions", icon='📈')

def AdPost():
    st.sidebar.page_link("pages/13_Post_Ad.py", label="Post an Ad", icon='📋')

def AdDelete():
    st.sidebar.page_link("pages/14_Delete_Ad.py", label="Delete an Ad", icon='❌')

#### ------------------------ Deal Admin Role ------------------------
def DealAdminNav():
    st.sidebar.page_link("pages/21_Deal_Information.py", label='Deal Information', icon='🏨')
    st.sidebar.page_link("pages/22_Deal_Impressions.py", label='Deal Impressions', icon='📈')
    st.sidebar.page_link("pages/23_Post_Deal.py", label="Post a Deal", icon='📋')
    st.sidebar.page_link("pages/24_Delete_Deal.py", label="Delete a Deal", icon='❌')



# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width = 300)

    # If there is no logged in user, redirect to the Home (Landing) page
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('Home.py')
        
    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        #  If the user role is a traveler
        if st.session_state['role'] == 'traveler':
           TravelerHomeNav()
           TripsNav()
           CountriesNav()
           PromosNav()
           CostPred()

        # If the user role is an advertiser
        if st.session_state['role'] == 'advertiser':
            AdInfoNav()
            AdImpNav() 
            AdPost()
            AdDelete()

        
        # If the user is a deal administrator
        if st.session_state['role'] == 'deal_admin':
            DealAdminNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')

