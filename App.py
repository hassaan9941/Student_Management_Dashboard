import streamlit as st
import pandas as pd

students = pd.read_csv('students.csv')
st.title("Student Managment System")
st.write("Welcome to student managment system")
# dashboard metrices
def total_students(data):
    return len(data)


def avg_gpa(data):
    return data["GPA"].mean()


def department_count(data):
    result = data["Department"].nunique()
    print(result)
    print(type(result))
    return result


def graduation_count(data):
    return data["GraduationYear"].value_counts().sort_index()

def department_graph(data):
    return data["Department"].value_counts()

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.metric("Total Students", total_students(students))

with col2:
    st.metric("Average GPA", round(avg_gpa(students), 2))
with col3:
    st.metric("Departments", department_count(students))
st.subheader("Student Records")
st.dataframe(students)
st.subheader("🎓 Students by Graduation Year")
graduation_data = graduation_count(students)
st.dataframe(
     graduation_data,
    width=350,
    hide_index=False
)
st.subheader("🏫 Students by Department")
department_data = department_graph(students)
st.bar_chart(department_data)