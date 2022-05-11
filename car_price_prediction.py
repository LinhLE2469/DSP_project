#!/usr/bin/env python
# coding: utf-8

# In[30]:


import streamlit as st
#import plotly_express as px
import pandas as pd

#configuration

#@app.route('/predict',methods=["Get"])
def car_price_predictor(year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner):
    
   
    prediction=price_finder.predict([[year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]])
    print(prediction)
    return prediction


def main():
    st.set_option('deprecation.showfileUploaderEncoding', False)

    #title of the app
    st.title("Predict car_price")
    # add a sidebar
    st.sidebar.subheader("Setting")
    #setup file upload
    uploaded_file = st.sidebar.file_uploader(label="Upload your csv or Excel file",type=["csv","xlsx"])

    global df

    if uploaded_file is not None:
        print(uploaded_file)
        print('the file is uploaded!')
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            df = pd.read_excel(uploaded_file)
    try: 
        st.write(df)
    except Exception as e:
        print(e)
        st.write("Please upload file to the application")


    result=0
    
    if st.button("Predict"):
        result=car_price_predictor(year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner)
    st.success('The output is {} lacks'.format(result))


if __name__=='__main__':
        main()





# In[ ]:




