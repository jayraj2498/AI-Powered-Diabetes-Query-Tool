from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure GenAI Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to Load Google Gemini Model and Provide Queries as Response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to Retrieve Query from the Database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name STUDENT and contains the following columns:
    - STUDENT_ID (INTEGER)
    - NAME (VARCHAR)
    - DATE_OF_BIRTH (DATE)
    - CLASS (VARCHAR)
    - SECTION (VARCHAR)
    - MATH_MARKS (INT)
    - ENGLISH_MARKS (INT)
    - SCIENCE_MARKS (INT)
    - ATTENDANCE_PERCENTAGE (FLOAT)

    Here are some examples of how to convert English questions to SQL queries:

    Example 1:
    Question: How many students are there in total?
    SQL Query: SELECT COUNT(*) FROM STUDENT;

    Example 2:
    Question: What are the names and classes of all students in the '10th Grade'?
    SQL Query: SELECT NAME, CLASS FROM STUDENT WHERE CLASS = '10th Grade';

    Example 3:
    Question: Show the details of students who scored more than 90 in Math.
    SQL Query: SELECT * FROM STUDENT WHERE MATH_MARKS > 90;

    Example 4:
    Question: List the names of students with an attendance percentage above 75%.
    SQL Query: SELECT NAME FROM STUDENT WHERE ATTENDANCE_PERCENTAGE > 75.0;

    Example 5:
    Question: What are the names and marks in English for students in section 'A'?
    SQL Query: SELECT NAME, ENGLISH_MARKS FROM STUDENT WHERE SECTION = 'A';

    Please convert the following question into an SQL query. Make sure the SQL query does not contain any backticks or the word "sql" in the output.
    """
]

# Streamlit App
st.set_page_config(page_title="Student Database SQL query")
st.header("Gemini App To Retrieve SQL Student Database ") 


question = st.text_input("Enter your Student databse  query:", key="input")

submit = st.button("Ask the question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    sql_result = read_sql_query(response, "student.db")
    st.subheader("The Response is")
    for row in sql_result:
        # Convert tuple to string and strip parentheses
        row_str = str(row).strip("()")  # Remove parentheses
        st.write(row_str)
