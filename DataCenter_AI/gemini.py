import time

from google import genai
from google.genai import errors

from config import GEMINI_API_KEY

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not configured.")

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt: str):

    max_attempts = 3

    for attempt in range(max_attempts):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt,
            )

            return response.text

        except errors.ServerError as e:

            if attempt == max_attempts - 1:
                raise RuntimeError(
                    "Gemini is temporarily unavailable (503). "
                    "Please try again in a moment."
                ) from e

            time.sleep(2 ** attempt)
