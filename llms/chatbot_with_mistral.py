import os
from dotenv import load_dotenv
from mistralai import Mistral


load_dotenv()

if __name__ == '__main__':
    api_key = os.getenv('MISTRAL_API_KEY')
    if api_key is None:
        print("You need to set")
        exit(1)

    print("api key is :{}".format(api_key))

    model = "mistral-large-latest"

    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "What is the capital of madhya pradesh?",
            },
            {
                "role": "user",
                "content": "What is the capital of Jammu kashmir?",
            },
        ]
    )
    print(chat_response.choices[0].message.content)