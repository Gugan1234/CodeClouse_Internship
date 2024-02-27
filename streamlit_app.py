import streamlit as st
import pickle
import numpy as np
import warnings

 
warnings.filterwarnings('ignore')  



load_model = pickle.load(open('Train_model.sav','rb'))

def segment(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)
    prediction = load_model.predict(input_data_reshape)
    if (prediction == 1):
        return "The customer belongs to 1th crew"
    if (prediction == 2):
        return "The customer belongs to 2th crew"
    if (prediction == 3):
        return "The customer belongs to 3th crew"
    if (prediction == 4):
        return "The customer belongs to 4th crew"
    if (prediction == 5):
        return "The customer belongs to 5th crew"

st.title("""Customer Segmentation Tool""")

def main():
    #Genre,Age,Annual_Income_k,Spending_Score_1_100
    Genre = st.selectbox('Enter the Customer Gender', (0,1))
    Age = st.slider('Enter the Customer Age', 10,150)
    Annual_Income_k = st.slider('Enter the Customer Annual Income',3,80)
    Spending_Score_1_100 = st.slider('Enter the Customer Spending Score',1,100)

    seg = ''


    if st.button('Customer Segmentation'):
        seg = segment([Genre,Age,Annual_Income_k,Spending_Score_1_100])
        
    st.success(seg)


if __name__=='__main__':
    main()