from openai import OpenAI
import os

api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)
messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

while True:
    message = input("User: ")
    if message== "exit":
        print("exiting.......")
        exit()
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
       
        response_text = chat.choices[0].message.content
        print(f"ChatGPT: {response_text}")
        messages.append({"role": "assistant", "content": response_text})
