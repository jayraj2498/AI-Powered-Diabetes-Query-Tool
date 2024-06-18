# AI-Powered-Diabetes-Query-Tool 

# Diabetes Data Query Assistant

## Overview

The **Diabetes Data Query Assistant** is an interactive web application built using Streamlit and Google Gemini's generative AI. It allows users to input natural language queries related to a diabetes patient dataset and receive corresponding SQL query results. This app facilitates easy exploration and analysis of patient data stored in a SQLite database.

## Features

- **Natural Language Querying**: Convert plain English questions into SQL queries.
- **Comprehensive Patient Data**: Query detailed information about patients including age, BMI, blood glucose levels, and more.
- **Interactive Interface**: User-friendly Streamlit interface to input questions and display results.

## Table Schema

The `diabetes_prediction` table contains the following columns:

1. `gender` (VARCHAR): Gender of the patient (Male or Female).
2. `age` (FLOAT): Age of the patient in years.
3. `hypertension` (INT): Indicates if the patient has hypertension (1 for yes, 0 for no).
4. `heart_disease` (INT): Indicates if the patient has heart disease (1 for yes, 0 for no).
5. `smoking_history` (VARCHAR): Smoking history of the patient.
6. `bmi` (FLOAT): Body Mass Index (BMI) of the patient.
7. `HbA1c_level` (FLOAT): HbA1c level of the patient.
8. `blood_glucose_level` (INT): Blood glucose level of the patient.
9. `diabetes` (INT): Indicates if the patient has diabetes (1 for diabetic, 0 for non-diabetic).

## Example Queries

Here are some example questions and their corresponding SQL queries:

1. **Question**: How many patients are there in total?
   - **SQL Query**: `SELECT COUNT(*) FROM diabetes_prediction;`

2. **Question**: What are the ages and BMIs of all male patients?
   - **SQL Query**: `SELECT age, bmi FROM diabetes_prediction WHERE gender = 'Male';`

3. **Question**: Show the details of patients with diabetes who have a BMI greater than 30.
   - **SQL Query**: `SELECT * FROM diabetes_prediction WHERE diabetes = 1 AND bmi > 30;`

4. **Question**: List the IDs and blood glucose levels of patients with blood glucose levels above 120.
   - **SQL Query**: `SELECT patient_id, blood_glucose_level FROM diabetes_prediction WHERE blood_glucose_level > 120;`

5. **Question**: Retrieve the HbA1c levels of patients aged between 40 and 50.
   - **SQL Query**: `SELECT HbA1c_level FROM diabetes_prediction WHERE age BETWEEN 40 AND 50;`

## Setup and Installation

Follow these steps to set up and run the Diabetes Data Query Assistant:

### Prerequisites

- Python 3.8 or higher
- `pip` package manager

### Libraries

Install the required Python libraries using the following command:

```bash    
pip install streamlit pandas google-generativeai python-dotenv sqlite3



#### Usage Instructions
Enter your question about diabetes patient data in the input box provided.
Click on the "Ask the question" button to generate and execute the SQL query.
View the results of your query in the table displayed below the input bo
