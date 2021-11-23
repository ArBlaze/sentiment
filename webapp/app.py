import streamlit as st
from predict_page import review_page
from tools_used import tools_used
from about import about_page


pages = st.sidebar.selectbox("Menus", ("About", "Prediction", "Tools Used"))



if pages == "About":
    about_page()
elif pages == "Prediction":
    review_page()
elif pages == "Tools Used":
    tools_used()
