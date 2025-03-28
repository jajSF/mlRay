from openai import OpenAI

# Initialize client
client = OpenAI(base_url="http://localhost:8000/v1", api_key="fake-key")

# Basic chat completion with streaming
reponse = client.chat.completions.create(
    model="qwen-0.5b",
    messages=[{"role":"user", "content":"Hello!"}],
    stream=True
)

for chunk in reponse:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flash=True)