print(">>> Loading NEW gemini.py <<<")
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are an experienced Site Reliability Engineer.

Analyze the given application/Kubernetes logs.

Return your response in the following format:

Root Cause:
Severity:
Possible Causes:
Recommendation:

Keep the response concise and technical.
"""

def analyze_logs(logs: str):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"{SYSTEM_PROMPT}\n\nLogs:\n{logs}"
    )

    return response.text
api_key = os.getenv("GEMINI_API_KEY")
print("API Key Loaded:", api_key[:10] + "..." if api_key else "NOT FOUND")

client = genai.Client(api_key=api_key)
