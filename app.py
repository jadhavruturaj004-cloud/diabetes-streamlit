
import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Diabetes Prediction App")

preg = st.number_input("Pregnancies", 0, 20, 1)
glu = st.number_input("Glucose", 0, 300, 120)
bp = st.number_input("Blood Pressure", 0, 200, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
ins = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 10, 100, 30)

if st.button("Predict"):
    data = np.array([[preg, glu, bp, skin, ins, bmi, dpf, age]])
    result = model.predict(data)[0]
    if result == 1:
        st.error("High chance of Diabetes")
    else:
        st.success("Low chance of Diabetes")

