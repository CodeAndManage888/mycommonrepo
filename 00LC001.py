from openai import OpenAI
client = OpenAI(api_key = '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')

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['message']['content'].strip()

prompt = "Tell me a joke"
response_text = chat_with_gpt(prompt)
print("ChatGPT:", response_text)
