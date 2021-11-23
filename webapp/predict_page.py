import numpy as np
import pandas as pd
import streamlit as st
import pickle


loaded_model = pickle.load(open
                           ("C:/Users/lance/Desktop/Folder/Folder/Folder/" +
                            "Python/IMDB Sentiment/webapp/model/imdb.pkl",
                            "rb"))

loaded_vector = pickle.load(open
                            ("C:/Users/lance/Desktop/Folder/Folder/Folder/" +
                             "Python/IMDB Sentiment/webapp/model/tfidf1.pkl",
                             'rb'))



def review_page ():
    st.title("IMDB Review Sentiment Prediction")
    input = st.text_input("Please enter a movie review:")
    if input:
        result = "This is a " + loaded_model.predict(
                loaded_vector.transform([input]))[0] + " review."
        st.text(result)
    
