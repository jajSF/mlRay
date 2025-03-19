import requests
import time

english_text = (
    "It was the best of times, it was the worst of times, it was the age"
    "of wisdom, it was the age of foolishness, it was the epoch of belief"
)

start_time = time.time()
response = requests.post("http://127.0.0.1:8000", json=english_text)
french_text = response.text
stop_time = time.time()

print("time taken: ", stop_time - start_time)
print(french_text)