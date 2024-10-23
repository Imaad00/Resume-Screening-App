import mysql.connector

# MySQL connection (XAMPP configuration)
db = mysql.connector.connect(
    host="localhost",  
    user="root",       
    password="",       
    database="resume_db"  
)

cursor = db.cursor()

# Function to store resume in the database
def store_resume(candidate_name, resume_text):
    insert_query = "INSERT INTO resumes (candidate_name, resume_text) VALUES (%s, %s)"
    cursor.execute(insert_query, (candidate_name, resume_text))
    db.commit()
    return cursor.lastrowid 

# Function to store result in the database
def store_result(resume_id, prediction_id, category_name):
    prediction_id = int(prediction_id)
    
    insert_query = "INSERT INTO results (resume_id, prediction_id, category_name) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (resume_id, prediction_id, category_name))
    db.commit()
