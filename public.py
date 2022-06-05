import requests

url = 'http://localhost:8000/api/public/?public=True'  # Полный адрес эндпоинта
response = requests.get(url)  # Делаем GET-запрос
# Поскольку данные пришли в формате json, переведем их в python
response_on_python = response.json()
# Запишем полученные данные в файл public.txt
with open('public.txt', 'w') as file:
    for note in response_on_python:
        file.write(
            f"Title: {note['title']}, "
            f"public: {note['public']}, "
            f"author: {note['author']}\n"
        )
# Вывод на экран
for note in response_on_python:
    print(f"Title: {note['title']}, "
            f"public: {note['public']}, "
            f"author: {note['author']}\n"
          )