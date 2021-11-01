import streamlit as st
import app1
import app2
import app3
import app4
import app5
import app6

PAGES = {
    "About": app1 ,
    "Technology" : app2 ,
    'Speech to Text': app3 ,
    "Mental Health Monitor": app4 ,
    "Style Transfer": app5 ,
    'Deep Dream'  : app6
}
st.sidebar.title('Helping Hands')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()