import streamlit as st
import pandas as pd
data=pd.read_csv(r"C:\Users\raji\Desktop\final project\Code\score.csv")
whole_data=pd.read_csv(r"C:\Users\raji\Desktop\final project\Code\final_data.csv",index_col=0)

st.header("Data Used")
st.dataframe(whole_data.head())

st.header("Model Performance")
st.dataframe(data)