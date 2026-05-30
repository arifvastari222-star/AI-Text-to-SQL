import streamlit as st

from ai.sql_generator import generate_sql
from database.query_executor import execute_query
from utils.sql_validator import validate_sql

st.set_page_config(
    page_title="AI Text-to-SQL Agent",
    page_icon="🤖"
)

st.title("🤖 AI Text-to-SQL Agent")

question = st.text_input(
    "Ask a question about your database:"
)

if question:

    try:

        sql = generate_sql(question)

        validate_sql(sql)

        st.subheader("Generated SQL")

        st.code(sql, language="sql")

        df = execute_query(sql)

        st.subheader("Results")

        st.write(f"Total rows returned: {len(df)}")

        st.dataframe(df.head(100))

    except Exception as e:

        st.error(str(e))