import streamlit as st
import pickle as pk
import pandas as pd

simi = pk.load(open('simimovie.pkl', 'rb'))

movies_dict = pk.load(open('chitrapat_dakhva.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

st.title("Chitrapat Suchava Pranali")

def recommend(w):

    mi = movies[movies['title'] == w].index[0]
    sr = sorted(enumerate(simi[mi]),reverse=True,key= lambda x:x[1])[1:6]
    
    g = []
    for i in sr:
        g.append(i[0])

    k = []
    for i in g:
        k.append(movies['title'][i]) 

    return k

option = st.selectbox('Tumchya Avdicha Chitrapat Liha....', movies['title'].values)

if st.button('Suchava'):
    p = recommend(option)

    for i in p:
        st.write(i)
     