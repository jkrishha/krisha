import streamlit as st
import pandas as pd 
st.title('machine learning')

st.write('this is a machine learning app')
df=pd.read_csv('https://github.com/dataprofessor/data/blob/master/penguins_cleaned.csv')
df
