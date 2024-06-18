import os
from dotenv import load_dotenv
import pandas as pd
import pymysql as sql
import sqlite3

# Load environment variables from .env file
load_dotenv()

# MySQL database credentials
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv('db')

def fetch_data_from_mysql(table_name):
    try:
        # Connect to MySQL database
        connection = sql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        
        # Fetch data from MySQL table into DataFrame
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, connection)
        
        print(f"Data fetched successfully from MySQL table '{table_name}':")
        print(df.head())
        
        connection.close()
        return df
    
    except Exception as e:
        print(f"Failed to fetch data from MySQL table '{table_name}'")
        print(e)
        return None

def save_data_to_sqlite(df, filename):
    try:
        # Connect to SQLite database (create it if it doesn't exist)
        conn = sqlite3.connect(filename)
        
        # Save DataFrame to SQLite database
        df.to_sql(name='diabetes_prediction', con=conn, if_exists='replace', index=False)
        
        conn.close()
        print(f"Data saved to SQLite database '{filename}' successfully")
    
    except Exception as e:
        print(f"Failed to save data to SQLite database '{filename}'")
        print(e)
        
        
        
# table name 
# Fetch data from MySQL table 'diabetes_prediction'
dataframe = fetch_data_from_mysql('diabetes_prediction')

# Save fetched data to SQLite database file 'diabetes.db' if successful
if dataframe is not None:
    print(dataframe.info()) 
    save_data_to_sqlite(dataframe, 'diabetes_data.db')



############### run sucessfully ########################### 


# import os
# from dotenv import load_dotenv
# import pymysql as sql
# import pandas as pd
# import sqlite3

# load_dotenv()

# host = os.getenv("host")
# user = os.getenv("user")
# password = os.getenv("password")
# db = os.getenv('db')

# def read_sql_data(table_name):
#     try:
#         mydb = sql.connect(
#             host=host,
#             user=user,
#             password=password,
#             db=db
#         )
#         print("Connection Established", mydb)
#         df = pd.read_sql_query(f'SELECT * FROM {table_name}', mydb)
#         print(df.head())
#         return df

#     except Exception as e:
#         print(f"Connection not established for table {table_name}")
#         print(e)
#         return None

# def save_data_as_db(df, filename):
#     try:
#         # Connect to SQLite database (it will create the database if it doesn't exist)
#         conn = sqlite3.connect(filename)
#         # Save the DataFrame to the SQLite database
#         df.to_sql('diabetes_prediction', conn, if_exists='replace', index=False)
#         conn.close()
#         print(f"Data saved to {filename}")
#     except Exception as e:
#         print(f"Failed to save data to SQLite database {filename}")
#         print(e)

# # Fetch data from MySQL database table 'diabetes_prediction'
# dataframe = read_sql_data('diabetes_prediction')

# # Save data to SQLite database file 'diabetes.db' if fetching was successful
# if dataframe is not None:
#     save_data_as_db(dataframe, 'diabetes.db')














# import os 
# from dotenv import load_dotenv 
# import pymysql as sql   
# import pandas as pd 

# load_dotenv()

# host= os.getenv("host")
# user= os.getenv("user") 
# password= os.getenv("password") 
# db=os.getenv('db')  


# def read_sql_data():
#     # logging.info("Reading SQL database started")
#     try:
#         mydb=pymysql.connect(
#             host=host,
#             user=user,
#             password=password,
#             db=db
#         )
#         print("Connection Established",mydb)
#         df=pd.read_sql_query('select * from fuelconsumption_modified',mydb)   # already present in the pandas 
#         print(df.head())

#         return df 
    
#     except Exception as e:
#         print("Connection not established") 
           