import requests

def ask_financial_llm(question, profile):

    prompt = f"""
You are an expert financial advisor.

Use the user's financial data to give PERSONALIZED advice.

User Financial Profile:
{profile}

User Question:
{question}

Instructions:
- Give specific advice based on income, expenses, savings, and debt
- Mention numbers (like how much to save or cut)
- Suggest investment ideas based on risk profile
- Keep it practical and actionable
- Do NOT give generic advice

Answer:
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()

        return result.get("response", "No response from AI")

    except Exception as e:
        return f"AI Error: {str(e)}"