from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import sqlite3
import pandas as pd 
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
    The SQL database has the table name is diabetes_prediction   and contains the following columns:
    Columns:
      1. gender (VARCHAR): Gender of the patient (Male or Female).
      2. age (FLOAT): Age of the patient in years.
      3. hypertension (INT): Indicates if the patient has hypertension (1 for yes, 0 for no).
      4. heart_disease (INT): Indicates if the patient has heart disease (1 for yes, 0 for no).
      5. smoking_history (VARCHAR): Smoking history of the patient.
      6. bmi (FLOAT): Body Mass Index (BMI) of the patient.
      7. HbA1c_level (FLOAT): HbA1c level of the patient.
      8. blood_glucose_level (INT): Blood glucose level of the patient.
      9. diabetes (INT): Indicates if the patient has diabetes (1 for diabetic, 0 for non-diabetic).

    Examples of SQL queries you can ask:
    
    Here are some examples of how to convert English questions to SQL queries:

    Example 1:
    Question: How many patients are there in total?
    SQL Query: SELECT COUNT(*) FROM diabetes_prediction;

    Example 2:
    Question: What are the ages and BMIs of all male patients?
    SQL Query: SELECT age, bmi FROM diabetes_prediction WHERE gender = 'Male';

    Example 3:
    Question: Show the details of patients with diabetes who have a BMI greater than 30.
    SQL Query: SELECT * FROM diabetes_prediction WHERE diabetes = 1 AND bmi > 30;

    Example 4:
    Question: List the IDs and blood glucose levels of patients with blood glucose levels above 120.
    SQL Query: SELECT patient_id, blood_glucose_level FROM diabetes_prediction WHERE blood_glucose_level > 120;

    Example 5:
    Question: Retrieve the HbA1c levels of patients aged between 40 and 50.
    SQL Query: SELECT HbA1c_level FROM diabetes_prediction WHERE age BETWEEN 40 AND 50;

    Please enter your question about the diabetes dataset in English, and I will convert it into a SQL query for you. 
    Ensure your SQL query does not contain any backticks or the word "sql" in the output.
    

    Please convert the following question into an SQL query. Make sure the SQL query does not contain any backticks or the word "sql" in the output.
    """
]

# Streamlit App
st.set_page_config(page_title="Diabetes Data Query Assistant", page_icon=":hospital:")
st.header("🏥 Gemini App To Retrieve Diabetes Patient Data 🩺")

question = st.text_input("Enter your question about diabetes patient data:", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    sql_query = response.strip().replace("```py", "").replace("```", "").strip()
    
    print("*" * 60)
    print("Generated SQL Query:")
    print(sql_query)
    print("*" * 60)
    
    conn = sqlite3.connect("diabetes_data.db")
    cur = conn.cursor()
    cur.execute(sql_query)
    sql_result = cur.fetchall()
    conn.close()
    
    st.subheader("The Response is")
    if sql_result:
        df = pd.DataFrame(sql_result, columns=[desc[0] for desc in cur.description])
        st.dataframe(df)
    else:
        st.write("No results found.")
