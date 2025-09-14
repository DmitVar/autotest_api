import json

user_data = {
    'name': 'Olga',
    'age': 47,
    'gender': 'female',
    'is_student': False
}

with open("json-exaple.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)

with open("json-user.json", "w", encoding="utf-8") as f:
    json.dump(user_data, f)

