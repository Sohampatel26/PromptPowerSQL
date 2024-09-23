from dotenv import load_dotenv
# LOADING ALL ENVIRONMENT VARIABLES IN OUR CASE GOOGLE GEMINI KEY
load_dotenv()

# INSERTING NECESSARY LIBRARIES
import os
import sqlite3
import streamlit as st
import google.generativeai as genai

# CONFIGURING GENAI KEY
genai.configure(api_key=os.getenv("GOOGLLE_API_KEY"))

# FUNCTION TO LOAD GOOGLE GEMINI MODEL AND GET THE QUERIES AS OUTPUT (RESPONSE)
def talk_to_gemini(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# FUNCTION TO QUERY THE DATABASE
def read_sql_query(sql, db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()  # Gets all the queried rows
    con.commit()
    con.close()
    return rows

# CREATING A PROMPT (MOST IMPORTANT)
prompt = [
    """
    You are an expert in converting English questions into SQL Queries.
    The SQL database is named STUDENT and has columns: NAME, CLASS, SECTION.

    FOR EXAMPLE:
    - EXAMPLE1: How many students are there? The generated SQL command should be:
      SELECT COUNT(*) FROM STUDENT;
    
    - EXAMPLE2: Get me the students that are in MDS. The SQL command should be:
      SELECT * FROM STUDENT WHERE SECTION = 'MDS';

    Sections are like the Degrees such as MDS , MCS, Btech and classes are sunjects like Computer Science, Data Science, ML etc
    The SQL code should be clean, without unnecessary symbols like ''' at the beginning or end, and no sql in the output text.
    Ensure the correctness of SQL syntax.
    """
]

# STREAMLIT APP
st.set_page_config(page_title="PromptPowerSQL", layout="centered", initial_sidebar_state="collapsed")

# HEADER
st.title("🔍 PromptPowerSQL")
st.markdown("""
## Query Your Database Effortlessly
Forget writing SQL queries manually. Just describe what you need, and we'll do the hard work for you.

### Example Queries You Can Try:
- *How many students are in Data Science?*
- *Show me all students in section MDS.*

Simply enter your question below and hit **Submit**.
""")

# USER INPUT FOR QUESTION
question = st.text_input("Enter your question here", key="input")

# SUBMIT BUTTON
submit = st.button("🚀 Submit")

# IF SUBMIT IS CLICKED
if submit:
    if question:
        with st.spinner('Generating SQL query and fetching results...'):
            # Calling the function to generate SQL from prompt and question
            response = talk_to_gemini(question, prompt)
            st.subheader("Generated SQL Query:")
            st.code(response, language='sql')  # Display the generated SQL

            # Running the SQL query on the database and displaying results
            results = read_sql_query(response, "student.db")
            if results:
                st.subheader("Queried Results:")
                # Display each row in the result list
                for row in results:
                    # Assuming row is a tuple or list, and each entry is a value
                    st.write(row[0])  # Display the first item in each row (adjust if needed)
            else:
                st.warning("No results found or an error occurred. Please verify your input.")
    else:
        st.warning("Please enter a question before submitting.")
# FOOTER
st.markdown("---")
st.caption("Created by Soham")
