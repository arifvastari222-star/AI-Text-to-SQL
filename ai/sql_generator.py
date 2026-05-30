import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_sql(question):

    with open("prompts/sql_prompt.txt", "r") as file:
        prompt_template = file.read()

    prompt = prompt_template.replace(
        "{question}",
        question
    )

    response = model.generate_content(prompt)

    sql = response.text.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()