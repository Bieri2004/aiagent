import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    # Prüfe, ob --verbose als letztes Argument übergeben wurde
    verbose = False
    if args[-1] == "--verbose":
        verbose = True
        args = args[:-1]  # Entferne das Flag aus der Prompt-Liste

    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, user_prompt, verbose)


def generate_content(client, messages, user_prompt, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print("Response:")
    print(response.text)
    if verbose:
        usage = response.usage_metadata
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {usage.prompt_token_count}')
        print(f'Response tokens: {usage.candidates_token_count}')


if __name__ == "__main__":
    main()


