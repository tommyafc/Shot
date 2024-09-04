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

with st.form(key='columns_in_form'):
 sq1 = st.selectbox("Team 1:",("Atalanta", "Bologna", "Cagliari","Como","Empoli","Fiorentina","Genoa","Hellas Verona","Inter","Juventus","Lazio","Lecce","Milan","Monza","Napoli","Parma","Roma","Torino","Udinese","Venezia"),)
 sq2 = st.selectbox("Team 2:",("Atalanta", "Bologna", "Cagliari","Como","Empoli","Fiorentina","Genoa","Hellas Verona","Inter","Juventus","Lazio","Lecce","Milan","Monza","Napoli","Parma","Roma","Torino","Udinese","Venezia"),)
 submitted = st.form_submit_button('Submit')


#url= 'https://fbref.com/en/comps/11/2024-2025/2024-2025-Serie-A-Stats'
#response = requests.get(url).text.replace('<!--', '').replace('-->', '')
#df = pd.read_html(response, header=1)[8]

fbref_file2 = glob.glob('s1.csv')[0]
fbref_dif = pd.read_csv(fbref_file2, index_col=None, header=0, sep=',',encoding='unicode_escape')
df=fbref_dif

#url= 'https://fbref.com/en/comps/11/2024-2025/2024-2025-Serie-A-Stats'
#esponse = requests.get(url).text.replace('<!--', '').replace('-->', '')
#df2 = pd.read_html(response, header=1)[9]

fbref_file2 = glob.glob('s2.csv')[0]
fbref_dif = pd.read_csv(fbref_file2, index_col=None, header=0, sep=',',encoding='unicode_escape')
df2=fbref_dif

df['Sh p90'] = df['Sh'] / df['90s']
df['ShA p90'] = df2['Sh'] / df2['90s']

df['path'] = df['Squad'] + '.png'
def getImage(path):
    return OffsetImage(plt.imread(path), zoom=0.2, alpha = 1)
# Set font and background colour
plt.rcParams.update({'font.family':'Avenir'})

f, ax = plt.subplots(figsize = (8,5))
f.set_facecolor("white")

ax.scatter(df['Sh p90'], df['ShA p90'], c='white',s = 1)
ax.set_ylabel('Shot Against per Match',size=8)
ax.set_xlabel('Shot per Match',size=8)

ax.margins(0.05,0.1)

#plt.grid()
ax.grid(color='lightgrey', linestyle="--", lw = 0.5)

plt.gca().invert_yaxis()

ax.spines['right'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')

plt.tick_params(axis='x', labelsize=9, color='#ccc8c8')
plt.tick_params(axis='y', labelsize=9, color='#ccc8c8')

ax.axhline(df['Sh p90'].median(),ls = '-', color = 'black', lw = 1, alpha = 0.5)
ax.axvline(df['ShA p90'].median(), ls = '-', color = 'black', lw = 1, alpha = 0.5)

for index, row in df.iterrows():
    ab = AnnotationBbox(getImage(row['path']), (row['Sh p90'], row['ShA p90']), frameon=False)
    ax.add_artist(ab)

plt.text(0.25,-0.18,"xG vs xG Against per Match | Serie A", c='black', size=11)
plt.text(0.25,-0.1,"Strong or Weak compared to the median value", c='black', size=7, style='italic')
plt.text(2,-0.05,"@Onesto_analyst - Data: FBREF", c='black', size=6)

plt.text(2,0.22,"Strong Attack", c='green', size=5, style='italic')
plt.text(2,0.17,"Strong Defence", c='green', size=5, style='italic')

plt.text(0.3,0.22,"Weak Attack", c='red', size=5, style='italic')
plt.text(0.3,0.17,"Strong Defence", c='green', size=5, style='italic')

plt.text(2,2,"Strong Attack", c='green', size=5, style='italic')
plt.text(2,1.95,"Weak Defence", c='red', size=5, style='italic')

plt.text(0.3,2,"Weak Attack", c='red', size=5, style='italic')
plt.text(0.3,1.95,"Weak Defence", c='red', size=5, style='italic')

im = plt.imread('SerieA.png')
im = OffsetImage(im, zoom=.10)
ab = AnnotationBbox(im, (0.03, 1.06), xycoords='axes fraction', frameon=False)
ax.add_artist(ab)

st.pyplot(f)

df=df.set_index('Squad')
casa= (df.loc[sq1,'Sh p90'] + df.loc[sq2,'ShA p90']) / 2
ospite= (df.loc[sq2,'Sh p90'] + df.loc[sq1,'ShA p90']) / 2


if sq1 == sq2:
    st.write("")
else:
    with st.columns(3)[1]:
        st.write('Tiri',sq1,':', casa)
        st.write('Tiri',sq2,':', ospite)
        st.write('Tiri Totali:', casa+ospite)
    




#streamlit run /Users/tommy14/Desktop/FDS/Onesto_analyst/App.py

