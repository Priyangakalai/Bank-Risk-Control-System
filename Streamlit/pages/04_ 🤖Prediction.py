import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import pickle
import numpy as np

# Load the model and encoder

st.header("Loan Prediction")
data=pd.read_csv(r"C:\Users\raji\Desktop\final project\Code\final_data.csv",index_col=0)
df=data.head()
with open(r"C:\Users\raji\Desktop\final project\Code\xgbfinal.pkl","rb" ) as XGBModel:
    xgb=pickle.load(XGBModel)
with open(r"C:\Users\raji\Desktop\final project\Code\labelencoder.pkl","rb") as encoder:
    label_encoder=pickle.load(encoder)
#st.dataframe(data.head())
col1, col2, col3 = st.columns(3)



def main():
 with col1:
    
    Gender = st.selectbox("CODE_GENDER",data["CODE_GENDER"].unique())
    OCCUPATION_TYPE = st.selectbox("OCCUPATION_TYPE",data["OCCUPATION_TYPE"].unique())
    INSURED_ON_APPROVAL = st.number_input("NFLAG_INSURED_ON_APPROVAL")
    Amount_Credit = st.number_input("AMT_CREDIT_y")
    
 with col2:
    Payment_type = st.selectbox("NAME_CONTRACT_TYPE_x", data["NAME_CONTRACT_TYPE_x"].unique())
    Total_Income = st.number_input("AMT_INCOME_TOTAL")
    Approval_status = st.selectbox("FLAG_LAST_APPL_PER_CONTRACT",data["FLAG_LAST_APPL_PER_CONTRACT"].unique())
    Amount_Credit_x = st.number_input("AMT_CREDIT_x")
 with col3:
    DOB= st.number_input("DAYS_BIRTH_YEARS")
    Amount_Credit_year = st.number_input("AMT_REQ_CREDIT_BUREAU_YEAR")
    OBS = st.number_input("OBS_30_CNT_SOCIAL_CIRCLE")


    input_data = pd.DataFrame({
            "NAME_CONTRACT_TYPE_x": [Payment_type],
            "CODE_GENDER": [Gender],
            "AMT_INCOME_TOTAL": [Total_Income],
            "AMT_CREDIT_x": [Amount_Credit_x],
            "OCCUPATION_TYPE": [OCCUPATION_TYPE],
            "OBS_30_CNT_SOCIAL_CIRCLE": [OBS],
            "AMT_REQ_CREDIT_BUREAU_YEAR": [Amount_Credit_year],
            "AMT_CREDIT_y": [Amount_Credit],
            "FLAG_LAST_APPL_PER_CONTRACT": [Approval_status],
            "NFLAG_INSURED_ON_APPROVAL": [INSURED_ON_APPROVAL],
            "DAYS_BIRTH_YEARS": [DOB],
        })
    for col in ["CODE_GENDER","NAME_CONTRACT_TYPE_x","OCCUPATION_TYPE","FLAG_LAST_APPL_PER_CONTRACT"]:
         input_data[col]=label_encoder[col].transform(input_data[col])

 with col1:
    if st.button("Predict"):
            prediction = xgb.predict(input_data)
            output = prediction[0]  # Extract the single prediction value
            st.success(f"The prediction is: {output}")
    

main()

