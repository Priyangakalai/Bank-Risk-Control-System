import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Header for the Streamlit App
st.header("Graph View")
col1, col2, col3 = st.columns(3)

data = pd.read_csv(r"C:\Users\raji\Desktop\final project\Code\Final_cleaned_data.csv")
with col1:
 fig_gender = plt.figure(figsize=(3, 2))
 sns.barplot(x=data["CODE_GENDER"], y=data["AMT_ANNUITY_x"])
 plt.title('Amount Annuity By Gender')
 st.pyplot(fig_gender)

 fig_amount=plt.figure(figsize=(3, 2))
 sns.histplot(data=data, x=data['AMT_CREDIT_x'], kde=True, bins=30,)
 plt.title('Distribution of Credit Amount')
 st.pyplot(fig_amount)

with col2:
 fig_contract = plt.figure(figsize=(3, 2))
 sns.barplot(x=data["NAME_CONTRACT_TYPE_x"], y=data["AMT_CREDIT_x"])
 plt.title('Amount Credit By Payment Type')
 st.pyplot(fig_contract)
 
 fig_loan=plt.figure(figsize=(3, 2))
 sns.countplot(data=data, x='NAME_INCOME_TYPE')
 plt.xticks(rotation=90)
 plt.title('occuption Count')
 st.pyplot(fig_loan)



with col3:

 fig_Credit=plt.figure(figsize=(2, 2))
 sns.scatterplot(data=data, x='AMT_CREDIT_x', y='AMT_ANNUITY_x', hue='CODE_GENDER')
 plt.title('Credit Amount vs. Annuity')
 st.pyplot(fig_Credit)

 fig_box=plt.figure(figsize=(3, 2))
 sns.boxplot(data=data, x='CODE_GENDER', y='AMT_INCOME_TOTAL')
 plt.title('Income Distribution by Gender')
 st.pyplot(fig_box)

