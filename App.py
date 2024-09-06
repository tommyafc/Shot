import streamlit as st
import pandas as pd
import numpy as np
import csv
import glob

st.set_page_config(page_title='Average Shot Predictor')

st.title("Serie A - Average Shot Predictor")
st.markdown("@onesto_analyst")
#st.write('I have published my first webapp that calculates the number of expected shots per game for each team, based on data from previous league games.')
#st.write('This tool can be used to identify favourable odds and potentially gain an advantage over bookmakers.')
#st.write('Use it well. 🤗')
#st.image("Juventus.png")

with st.form(key='columns_in_form'):
 sq1 = st.selectbox("Team 1:",("Atalanta", "Bologna", "Cagliari","Como","Empoli","Fiorentina","Genoa","Hellas Verona","Inter","Juventus","Lazio","Lecce","Milan","Monza","Napoli","Parma","Roma","Torino","Udinese","Venezia"),)
 sq2 = st.selectbox("Team 2:",("Atalanta", "Bologna", "Cagliari","Como","Empoli","Fiorentina","Genoa","Hellas Verona","Inter","Juventus","Lazio","Lecce","Milan","Monza","Napoli","Parma","Roma","Torino","Udinese","Venezia"),)
 submitted = st.form_submit_button('Submit')
 st.write('Update: 05.09.2024 - Data: WhoScored')



#url= 'https://fbref.com/en/comps/11/2024-2025/2024-2025-Serie-A-Stats'
#response = requests.get(url).text.replace('<!--', '').replace('-->', '')
#df = pd.read_html(response, header=1)[8]

fbref_file = glob.glob('s1.csv')[0]
fbref_dif = pd.read_csv(fbref_file, index_col=None, header=0, sep=',',encoding='unicode_escape')
df=fbref_dif

#url= 'https://fbref.com/en/comps/11/2024-2025/2024-2025-Serie-A-Stats'
#esponse = requests.get(url).text.replace('<!--', '').replace('-->', '')
#df2 = pd.read_html(response, header=1)[9]

fbref_file2 = glob.glob('s2.csv')[0]
fbref_dif2 = pd.read_csv(fbref_file2, index_col=None, header=0, sep=',',encoding='unicode_escape')
df2=fbref_dif2

df['Sh p90'] = df['Sh'] / df['90s']
df['ShA p90'] = df2['Sh'] / df2['90s']

df=df.set_index('Squad')
casa= (df.loc[sq1,'Sh p90'] + df.loc[sq2,'ShA p90']) / 2
ospite= (df.loc[sq2,'Sh p90'] + df.loc[sq1,'ShA p90']) / 2

casa = round(casa, 2)
ospite = round(ospite, 2)


if sq1 == sq2:
    st.write("")
else:
    with st.columns(3)[1]:
        st.write(sq1,'Shots:', casa)
        st.write(sq2,'Shots:', ospite)
        st.write('Total Shots:', casa+ospite)


with st.form(key='columns_in_forma'):
 h1 = st.selectbox("Home:",("Atalanta", "Bologna", "Cagliari","Como","Empoli","Fiorentina","Genoa","Hellas Verona","Inter","Juventus","Lazio","Lecce","Milan","Monza","Napoli","Parma","Roma","Torino","Udinese","Venezia"),)
 a2 = st.selectbox("Away:",("Atalanta", "Bologna", "Cagliari","Como","Empoli","Fiorentina","Genoa","Hellas Verona","Inter","Juventus","Lazio","Lecce","Milan","Monza","Napoli","Parma","Roma","Torino","Udinese","Venezia"),)
 submitted = st.form_submit_button('Submit')
 st.write('Update: 05.09.2024 - Data: WhoScored')

fbref_file22 = glob.glob('s_HA.csv')[0]
fbref_difa = pd.read_csv(fbref_file22, index_col=None, header=0, sep=',',encoding='unicode_escape')
dfha=fbref_difa

dhaf=dfha.set_index('Squad')
casa2= (dfha.loc[h1,'Sh HOME'] + dfha.loc[a2,'Sh AWAY A']) / 2
ospite2= (dfha.loc[a2,'Sh AWAY'] + dfha.loc[h1,'Sh HOME A']) / 2

print(h1,':', casa2, 'Tiri')
print(a2,':', ospite2, 'Tiri')
print('Tiri Totali:', casa2+ospite2)



#streamlit run /Users/tommy14/Desktop/FDS/Onesto_analyst/App.py

