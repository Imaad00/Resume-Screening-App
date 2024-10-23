import streamlit as st
import pickle
import re
import nltk
from sql import store_resume, store_result  # Import functions from sql.py

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')


clf = pickle.load(open('clf.pkl', 'rb'))
tfidfd = pickle.load(open('tfidf.pkl', 'rb'))

# Clean resume function
def clean_resume(resume_text):
    clean_text = re.sub(r'http\S+\s*', ' ', resume_text)
    clean_text = re.sub(r'RT|cc', ' ', clean_text)
    clean_text = re.sub(r'#\S+', '', clean_text)
    clean_text = re.sub(r'@\S+', '  ', clean_text)
    clean_text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    return clean_text

# Web app main function
def main():
    st.markdown("""
    <style>
    body {
        background-color: #f0f2f5;
        font-family: Arial, sans-serif;
    }
    .title {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 20px;
    }
    .file-uploader {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    .streamlit-button {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        margin-top: 10px;
    }
    .streamlit-button:hover {
        background-color: #2980b9;
    }
    input[type="text"] {
        width: 80%;
        padding: 10px;
        margin: 10px auto;
        border-radius: 5px;
        border: 1px solid #ccc;
        transition: border-color 0.3s ease;
    }
    input[type="text"]:focus {
        border-color: #3498db;
        outline: none;
    }
    .result {
        text-align: center;
        font-size: 20px;
        color: #27ae60;
        margin-top: 20px;
        animation: fadeIn 1s;
    }
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='title'>Resume Screening App</h1>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader('Upload Resume', type=['txt', 'pdf'])

    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            # If UTF-8 decoding fails, try decoding with 'latin-1'
            resume_text = resume_bytes.decode('latin-1')

        cleaned_resume = clean_resume(resume_text)

        candidate_name = st.text_input("Enter Candidate Name")

        if st.button("Submit", key="submit_button"):
            # Store resume in the database
            resume_id = store_resume(candidate_name, cleaned_resume)

            # Perform prediction
            input_features = tfidfd.transform([cleaned_resume])
            prediction_id = clf.predict(input_features)[0]

            # Category mapping
            category_mapping = {
                15: "Java Developer",
                23: "Testing",
                8: "DevOps Engineer",
                20: "Python Developer",
                24: "Web Designing",
                12: "HR",
                13: "Hadoop",
                3: "Blockchain",
                10: "ETL Developer",
                18: "Operations Manager",
                6: "Data Science",
                22: "Sales",
                16: "Mechanical Engineer",
                1: "Arts",
                7: "Database",
                11: "Electrical Engineering",
                14: "Health and Fitness",
                19: "PMO",
                4: "Business Analyst",
                9: "DotNet Developer",
                2: "Automation Testing",
                17: "Network Security Engineer",
                21: "SAP Developer",
                5: "Civil Engineer",
                0: "Advocate",
            }

            category_name = category_mapping.get(prediction_id, "Unknown")

            st.markdown(f"<div class='result'>Predicted Category: {category_name}</div>", unsafe_allow_html=True)

            # Store the result in the database
            store_result(resume_id, prediction_id, category_name)

# Run the Streamlit web app
if __name__ == "__main__":
    main()
