import streamlit as st
import pandas as pd 
st.title('machine learning')

st.write('this is a machine learning app')
with st.expander('Data'):
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
st.write('X')
X=df.drop('species',axis=1)
X
Y=df.species
Y
