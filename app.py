import streamlit as st
import pandas as pd
import pickle

st.title("Hospital Treatment Cost Prediction System")

# Load Model
pipe = pickle.load(open("hospital_pipe.pkl", "rb"))

# Sidebar Inputs
age = st.sidebar.number_input("Enter Age", min_value=1, max_value=100, value=25)

sex = st.sidebar.selectbox(
    "Select Gender",
    ["male", "female"]
)

bmi = st.sidebar.number_input(
    "Enter BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

children = st.sidebar.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

smoker = st.sidebar.selectbox(
    "Smoker",
    ["yes", "no"]
)

region = st.sidebar.selectbox(
    "Select Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

# Predict Button
if st.sidebar.button("Predict Cost"):

    st.write("### Selected Details")
    st.write(f"Age: {age}")
    st.write(f"Gender: {sex}")
    st.write(f"BMI: {bmi}")
    st.write(f"Children: {children}")
    st.write(f"Smoker: {smoker}")
    st.write(f"Region: {region}")

    myinput = pd.DataFrame(
        [[age, sex, bmi, children, smoker, region]],
        columns=["age", "sex", "bmi", "children", "smoker", "region"]
    )

    result = pipe.predict(myinput)

    st.success(f"Predicted Hospital Treatment Cost: ₹ {round(result[0])}")