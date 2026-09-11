import streamlit as st
import pandas as pd
students = pd.read_csv('students.csv')
st.title("🔎 Student Search")
st.write("Search for a student using their ID or name.")
search_type = st.selectbox(
     "Search by:",
    ["Student ID", "Name"]
)
if search_type == "Student ID":
    student_id = st.number_input(
        "Enter Student ID",
        min_value=1,
        value=None,
        step=0
        
    )
    if st.button("Search"):
        result = students[students["StudentID"] == student_id]
        if not result.empty:
            st.success("Student found!!")
            st.dataframe(result , hide_index=True)
        else :
            st.error("Student not found!!")
            
else:
    name = st.text_input("Enter the name")
    if st.button("Search"):
         result = students[
            students["Name"].str.contains(
                name,
                case=False,
                na=False
            )
        ]
         if not result.empty:
             st.success("Student Found")
             st.dataframe(result ,hide_index=True)
         else:
             st.error("Student Not Found")

st.subheader("➕ Add a Student")

with st.form("add_student_form"):

    student_id = st.number_input("Student ID", min_value=1, placeholder="Enter Student ID" ,value=None)

    name = st.text_input("Name" , placeholder="Enter name")

    age = st.number_input(
        "Age",
        min_value=1,
        value=None,
        max_value=100,
        placeholder="Enter Age"
    )

    email = st.text_input("Email" , placeholder="example@gmail.com")

    department = st.selectbox(
        "Department",
        students["Department"].unique()
    )

    gpa = st.number_input(
        "GPA",
        min_value=0.0,
        max_value=4.0,
        value=None,
        placeholder="Enter Student GPA(0.00)"
    )

    graduation_year = st.number_input(
        "Graduation Year",
        min_value=2000,
        
    )

    submit = st.form_submit_button("Add Student")


if submit:

    if student_id in students["StudentID"].values:

        st.error("Student ID already exists!")

    else:

        new_student = {
            "StudentID": student_id,
            "Name": name,
            "Age": age,
            "Email": email,
            "Department": department,
            "GPA": gpa,
            "GraduationYear": graduation_year
        }

        students.loc[len(students)] = new_student

        students.to_csv("students.csv", index=False)

        st.success("Student added successfully! 🎉")

                   
