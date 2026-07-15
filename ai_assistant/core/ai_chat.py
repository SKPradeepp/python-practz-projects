import requests

API_KEY = "YOUR_OPENROUTER_API_KEY"

URL = "https://openrouter.ai/api/v1/chat/completions"


def ask_ai(prompt):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:

        response = requests.post(
            URL,
            headers=headers,
            json=data,
            timeout=30
        )

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception:

        return "Sorry, I couldn't connect to the AI."