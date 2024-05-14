import requests
import os  # Import os to access environment variables
import openai

def call_openai_api():
    openai.api_key = os.getenv('TEST_API_KEY')  # Ensure the API key is set from environment variables
    response = openai.ChatCompletion.create(
      model="gpt-4o",
      messages=[
        {"role": "system", "content": "Write a code that will print Hello World in Ruby on Rails, JavaScript, Assembly, C++, C, BASIC"},
        {"role": "user", "content": ""},
        {"role": "assistant", "content": "Kamusta mundo!"}
      ],
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    print(response)  # Print the response to see the output

if __name__ == "__main__":
    call_openai_api()