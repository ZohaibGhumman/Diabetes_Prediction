#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 02:15:44 2022

@author: zohaibghumman
"""

import numpy as np
import pickle
import streamlit as st


#loading the saved model
loaded_model = pickle.load(open('/Users/zohaibghumman/Desktop/DeployingUsingStreamlit/trained_model_sav', 'rb'))

# Creating a function for prediction
def diabetes_prediction(input_data):
    
   

    #changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instace
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standerdize the input data
    #std_data = scaler.transform(input_data_reshaped)
    #print(std_data)

    predection = loaded_model.predict(input_data_reshaped)
    print(predection)
    if(predection[0]==0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
    
  
def main():
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    # getting the data from the user

    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('SkinThickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
    Age = st.text_input('Age of the person')
    
    
    # Code fore prediction
    diagnosis = ''
    
    
    # Creating a Button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    
    st.success(diagnosis)
    
    
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    