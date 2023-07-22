# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 12:30:27 2023

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 11:41:34 2023

@author: USER
"""

import numpy as np
import pickle
import streamlit as st

load_model = pickle.load(open('F:/deployment/heart_disease.sav','rb'))

def heart_disease_prediction(input_data):
    inp=np.asarray(input_data)
    inputt=inp.reshape(1,-1)
    prediction = load_model.predict(inputt)
    print(prediction)
    if (prediction[0] == 0):
        return'The person has no heart disease'
    else:
        return'The person has heart disease'

def main():
    st.title('heart disease prediction web app')
    col1,col2,col3 = st.columns(3)
  
    with col1:
        age = st.text_input('age of the person')
        trestbps = st.text_input('resting blood pressure')
        restecg = st.text_input('electro cardiographic results')
        oldpeak =  st.text_input('ST depression')
        thal =  st.text_input('thallium scintigraphy')
    with col2:
        sex = st.text_input('gender')
        chol = st.text_input('cholesterol')
        thalac = st.text_input('maximum heart rate')
        slope =  st.text_input('ST segment')
    with col3:
       cp = st.text_input('chest pain')
       fbs = st.text_input('fasting blood sugar level')
       exang = st.text_input('exercise-induced angina')
       ca =  st.text_input('coloured vessels')
     
    diagnosis = ' '
    if st.button('diagnosis test results'):
        diagnosis = heart_disease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalac,exang,oldpeak,slope,ca,thal])
    st.success(diagnosis)

if __name__ == '__main__':
    main()