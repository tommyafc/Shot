import streamlit as st
import pandas as pd
import numpy as np
import csv
import glob

st.set_page_config(page_title='Onesto Analyst')

st.title("ONESTO ANALYST")
st.write('I have published my first webapp that calculates the number of expected shots per game for each team, based on data from previous league games.')
st.write('This tool can be used to identify favourable odds and potentially gain an advantage over bookmakers.')
st.write('Use it well. 🤗')

st.image("https://i.postimg.cc/L8KqkdFC/Shot-Serie-A.png")

with st.columns(3)[1]:
    with st.form(key='columns_in_form'):
     sq1 = st.selectbox("Team 1:",("Atalanta", "Bologna", "Cagliari","Como","Empoli","Fiorentina","Genoa","Hellas Verona","Inter","Juventus","Lazio","Lecce","Milan","Monza","Napoli","Parma","Roma","Torino","Udinese","Venezia"),)
     sq2 = st.selectbox("Team 2:",("Atalanta", "Bologna", "Cagliari","Como","Empoli","Fiorentina","Genoa","Hellas Verona","Inter","Juventus","Lazio","Lecce","Milan","Monza","Napoli","Parma","Roma","Torino","Udinese","Venezia"),)
     submitted = st.form_submit_button('Submit')



#streamlit run /Users/tommy14/Desktop/FDS/Onesto_analyst/App.py

