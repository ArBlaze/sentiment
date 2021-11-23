import numpy as np
import pandas as pd
import streamlit as st
import pickle


tools = ["* JupyterLab", "* Spyder", "* Scikit-Learn"]

def tools_used():
    st.title("Tools Used")
    for li in tools:
        st.markdown(li)
        
    