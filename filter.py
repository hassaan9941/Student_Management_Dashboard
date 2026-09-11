import streamlit as st
import pandas as pd
st.title("Filters 🔍")
st.write("Filter students by GPA, Departments, Graduation year and Age")
students = pd.read_csv("students.csv")
departments = st.multiselect(
    "Filter by Department",
    students["Department"].unique()
)
age_range = st.slider(
    "Age Range",
    min_value=int(students["Age"].min()),
    max_value=int(students["Age"].max()),
    value=(
        int(students["Age"].min()),
        int(students["Age"].max())
    )
)
gpa_condition = st.selectbox(
    "GPA Condition",
    ["Greater than", "Less than", "Equal to"]
)
gpa_value = st.number_input(
    "GPA",
    min_value=0.0,
    max_value=4.0,
    value= None,
    placeholder=("Enter GPA")
)
graduation_year = st.selectbox(
    "Graduation Year",
    sorted(students["GraduationYear"].unique())
)
filtered_students = students    
if departments:
    filtered_students = students[
        students["Department"].isin(departments)
    ]
if gpa_condition == "Greater than":
    filtered_students = filtered_students[
        filtered_students["GPA"] > gpa_value
    ]

elif gpa_condition == "Less than":
    filtered_students = filtered_students[
        filtered_students["GPA"] < gpa_value
    ]

elif gpa_condition == "Equal to":
    filtered_students = filtered_students[
        filtered_students["GPA"] == gpa_value
    ]

if graduation_year:
    filtered_students = students[
        students["GraduationYear"] == graduation_year
    ]

elif age_range:
    filtered_students = students[
    (students["Age"] >= age_range[0]) &
    (students["Age"] <= age_range[1])
    ]

st.dataframe(filtered_students)