import requests

english_text = "Hello, how are you doing today?"

response = requests.post("http://127.0.0.1:8000/", json=english_text)
french_text = response.text

print(french_text)