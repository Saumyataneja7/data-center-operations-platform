from gemini import ask_gemini

def generate_answer(question, dataframe):

    prompt = f"""
You are an AI Operations Assistant for a Data Center.

The user asked:

{question}

The SQL query returned the following data:

{dataframe.to_markdown(index=False)}

Provide:

1. Executive Summary
2. Key Findings
3. Recommendations

Keep the answer concise and professional.
"""

    return ask_gemini(prompt)