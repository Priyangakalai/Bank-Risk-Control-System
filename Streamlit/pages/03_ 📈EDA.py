import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Header for the Streamlit App
st.header("Graph View")
col1, col2, col3 = st.columns(3)

data = pd.read_csv(r"C:\Users\raji\Desktop\final project\Code\Final_cleaned_data.csv")
with col1:
 
 payment=plt.figure(figsize=(5,5))
 sns.countplot(data=data,x="TARGET")
 plt.title("Payment difficulties")
 st.pyplot(payment)
 
 fig_gender = plt.figure(figsize=(5,5))
 sns.barplot(x=data["CODE_GENDER"],y=data["AMT_INCOME_TOTAL"])
 plt.title('Income By Gender')
 st.pyplot(fig_gender)

 fig_amount=plt.figure(figsize=(5,5))
 sns.barplot(data=data, x='NAME_CONTRACT_TYPE_x', y='AMT_CREDIT_x')
 plt.title('Amount Credit By Payment Type')
 st.pyplot(fig_amount)

 fig_con= plt.figure(figsize=(5,5))
 sns.countplot(x=data["CODE_GENDER"])
 plt.title('Bank account holder by gender')
 st.pyplot(fig_con)

with col2:
 fig_contract = plt.figure(figsize=(5,5))
 sns.boxplot(data=data, x='AMT_INCOME_TOTAL')
 plt.title('Income')
 st.pyplot(fig_contract)
 
 fig_loan=plt.figure(figsize=(5,5))
 sns.histplot(data['DAYS_BIRTH_YEARS'], bins=20, kde=True, color='blue')
 plt.title('Age Distribution')
 st.pyplot(fig_loan)

 fig_Credit=plt.figure(figsize=(5,5))
 sns.countplot(y='OCCUPATION_TYPE', data=data, order=data['OCCUPATION_TYPE'].value_counts().index)
 plt.title('Distribution of Occupation Types')
 st.pyplot(fig_Credit)

 fig_box=plt.figure(figsize=(5,5))
 sns.boxplot(data=data, x='TARGET', y='AMT_CREDIT_x')
 plt.title('Credit Amount by Target')
 st.pyplot(fig_box)

