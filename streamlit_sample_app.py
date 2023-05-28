import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(layout="wide")

filename = 'diabetes_prediction_model.sav'

#df = df2[['Price', 'Age_08_04', 'KM', 'Fuel_Type', 'Automatic', 'Gears']]
loaded_model = pickle.load(open(filename, 'rb'))

st.title('Diabetes Prediction Boosting Web App')
st.write('This is a web app to predict the if you are prone to being diabetec\
        several features that you can see in the sidebar. Please adjust the\
        value of each feature. After that, click on the Predict button at the bottom to\
        see the prediction of the regressor.')
gender_Male = 0
gender_Female = 0
gender_Other = 0
hypertension_yes = 0
hypertension_no = 0
heart_disease = 0
smoking_history_current = 0
smoking_history_former = 0
smoking_history_never = 0


with st.sidebar:
    age         = st.number_input(label='Your Age',min_value = 0.0,
                        max_value = 110.0 ,
                        value = 25.0,
                        step = 1.0)      

    HbA1c_level          = st.slider(label = 'Average Blood Sugar Level', min_value = 3.0,
                        max_value = 12.0 ,
                        value = 6.0,
                        step = 0.1)
                        
    bmi          = st.slider(label = 'Your Body Mass Index', min_value = 15.0,
                        max_value = 35.0 ,
                        value = 20.0,
                        step = 0.5)

    blood_glucose_level  = st.slider(label = 'Your Blood Glucose Level', min_value = 50,
                        max_value = 250 ,
                        value = 100,
                        step = 5)                        





    gender   = st.radio('Gender', ('Male','Female','Other'))
    if (gender == 'Male'):
        gender_Male = 1
    elif (gender == 'Other'):
        gender_Other = 1
    else:
        gender_Female = 1

    hypertension_value   = st.radio('Hypertension', ('Yes','No'))
    if (hypertension_value == 'Yes'):
        hypertension = 1  

    heart_disease_value   = st.radio('Heart Disease', ('Yes','No'))
    if (heart_disease_value == 'Yes'):
        heart_disease = 1     

    smoking_history   = st.radio('Smoking History', ('current','never','former'))
    if (smoking_history == 'former'):
        smoking_history_former = 1
    elif (smoking_history == 'never'):
        smoking_history_never = 1
    else:
        smoking_history_current = 1         
        
    

    smoking_history   = st.radio('Smoking History', ('current','never','former'))


features = {
  'age':age,
  'hypertension':hypertension,
  'heart_disease':heart_disease,
  'HbA1c_level':HbA1c_level,
  'bmi':bmi,
  'blood_glucose_level':blood_glucose_level,
  'gender_Male':gender_Male,
  'gender_Other':gender_Other,
  'smoking_history_former':	smoking_history_former,
  'smoking_history_never':	smoking_history_never}
  

features_df  = pd.DataFrame([features])

st.table(features_df)
col1, col2 = st.columns((1,2))

with col1:
    prButton = st.button('Predict')
with col2: 
    if prButton:    
        prediction = loaded_model.predict(features_df)    
        st.write(' Based on feature values, your diabetes value is '+ str(int(prediction)))
