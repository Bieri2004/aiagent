import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model_name = "gemini-2.0-flash-001"

    # System Prompt festlegen
    system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

    # Prompt aus Kommandozeile holen
    args = sys.argv[1:]
    if not args:
        print("Usage: python main.py \"your prompt here\"")
        sys.exit(1)
    user_prompt = " ".join(arg for arg in args if not arg.startswith("--"))

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )

    print(response.text)

if __name__ == "__main__":
    main()


