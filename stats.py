import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
students = pd.read_csv("students.csv")
st.title("📊 Student Analytics")
st.write(
    """Explore student data through statistics and visualizations. Analyze department distribution, graduation trends, GPA performance, and other key insights from the student records.
"""
)
# for departments
st.subheader("Student by Departments")
departments_data = students["Department"].value_counts()
st.bar_chart(departments_data)
# for Graduation year
st.subheader("Students by GraduationYear")
grad_yr = students["GraduationYear"].value_counts()
st.bar_chart(grad_yr)
# for GPA distribution
st.subheader("📈 GPA Distribution")
fig, ax = plt.subplots()

ax.hist(
    students["GPA"],
    bins=[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
)

ax.set_xlabel("GPA")
ax.set_ylabel("Number of Students")
ax.set_title("GPA Distribution")

st.pyplot(fig)
# for GPA by departments
st.subheader("📊 Average GPA by Department")

avg_gpa_dept = students.groupby("Department")["GPA"].mean()

fig, ax = plt.subplots(figsize=(12,6))

ax.bar(avg_gpa_dept.index, avg_gpa_dept.values)

ax.set_xlabel("Department")
ax.set_ylabel("Average GPA")
ax.set_title("Average GPA by Department")

st.pyplot(fig)