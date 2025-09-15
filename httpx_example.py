import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())

data = {
    'userId': 1,
    'title': 'New task',
    'completed': False
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)
print(response.json())

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.request.headers)
print(response.json())


address_data = {
    "city": "Minsk",
    "street": "Svyzistov"
}
response = httpx.post("https://httpbin.org/post", data=address_data)
print(response.status_code)
print(response.request.headers)
print(response.json())

headers = {"Authorization": "Bearer my_secret_key"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.request.headers)
print(response.json())

response = httpx.get("https://jsonplaceholder.typicode.com/todos?userId=1")
print(response.status_code)
for item in response.json():
    print(item['id'], item['title'], item['completed'])

params = {"userId": 2}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.status_code)
print(response.status_code)
for item in response.json():
    print(item['id'], item['title'], item['completed'])

files = {"file": open("example.txt", "rb")}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.status_code)
print(response.json())

with httpx.Client() as client:
    response1 = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = httpx.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())
print(response2.json())

client = httpx.Client(headers={"Authorization": "Bearer my_secret_key"})
response = client.get("https://httpbin.org/get")
print(response.json())
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid_url")
    response.raise_for_status()
except httpx.HTTPError as e:
    print(f"Http error: {e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print(f"Запрос превысил лимит времени")