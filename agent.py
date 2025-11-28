import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def student_agent(user_input: str) -> str:
    if not user_input or not user_input.strip():
        return "Please type something so I can help 😊"

    if not api_key:
        return "⚠️ OPENAI_API_KEY is missing. Please add it to your .env file."

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=(
                "You are EduMate, an expert AI tutor for students. "
                "Answer clearly and simply. "
                "You can answer questions about AI, ML, SQL, Deep Learning, "
                "OOPS, DSA, Computer Networks, Operating Systems, and programming.\n\n"
                f"Student question: {user_input}"
            ),
        )

        return response.output[0].content[0].text.strip()

    except Exception as e:
        return f"Oops, something went wrong: {e}"
