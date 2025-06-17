import requests

url = "https://tds-mkg513boq-23f3001930.vercel.app/query"

payload = {
    "question": "What is the purpose of pandas pivot_table?",
    "image": None  # or you can omit this line entirely if not sending an image
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
try:
    print("Response JSON:", response.json())
except ValueError:
    print("Response content is not valid JSON:")
    print(response.text)
