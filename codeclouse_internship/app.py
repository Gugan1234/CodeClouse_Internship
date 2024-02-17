import numpy as np
import pickle 
import streamlit as st

loaded_model=pickle.load(open('Treained_model.sav','rb'))

def heart_disease(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    if(prediction[0]==0):
        return "The person has Heart Disease"
    else:
        return "The person does not have heart disease"
st.title("""Heart Disease Prediction""")
st.sidebar.title("""Choose the Inputs to implement""")

#creating main function for web page
def main():
    age = st.sidebar.slider('Age of the Person',1,100)
    sex = st.sidebar.selectbox('Sex',(0,1))
    cp = st.sidebar.selectbox('CP of the person',(0,1,2,3))
    trestbps = st.slider('TrestBPS of the Person',120,200)
    chol = st.slider("Chol of the person",1,250)
    fbs = st.sidebar.selectbox('Fbs of the person',(0,1))
    restecg = st.sidebar.selectbox('Restecg of the Person',(0,1,2,3))
    thalach = st.slider('Thalach of the Person',1,302)
    exang = st.sidebar.selectbox('Exang of the Person',(0,1))
    oldpeak = st.slider('oldpeak of the Person',0.0,10.10)
    slope = st.selectbox('Slope of the Persons Heart',(0,1,2))
    ca = st.selectbox('Calcium of the patient heart',(0,1,2,3,4))
    thal = st.sidebar.selectbox('Thal of the Person', (0,1,2,3))

    #Code to predict
    disease = ''

    if st.button('Heart Disease Result'):
        disease = heart_disease([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])

    st.success(disease)

if __name__ == '__main__':
    main()


    