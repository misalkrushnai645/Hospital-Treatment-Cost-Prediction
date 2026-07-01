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
#BMI Status 
if bmi 18.5:
    st.info("BMI Status : Underweight")
elif bmi < 25:
    st.success("BMI Status: Normal")
elif bmi < 30:
    st.warning("BMI Status : Overweight")
else:
    st.error("BMI Status: Obese")

# Health Risk
if smoker == "yes": 
    st.error("Health Risk High")
else:
    st.success("Health Risk: Low")

# Health Tip
if smoker == "yes":
    st.warning(" Tip: Quit smoking to reduce future health risks.")
else:
    st.info(" Tip: Maintain a healthy lifestyle.")
    st.markdown("---") st.caption("Developed by Krushnai Misal")
