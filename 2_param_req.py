#   Задание 2: Параметры запрос
#1. Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
#2. Отправьте GET-запрос с параметром `userId`, равным `1`.
#3. Распечатайте полученные записи.

import requests

user_id = 1
url = f'https://jsonplaceholder.typicode.com/posts?userId={user_id}'

response = requests.get(url)

if response.status_code == 200:
    print('Получено', len(response.json()), 'записей')
    for post in response.json():
        print(post['id'], post['title'])
else:
    print(f'Ошибка при выполнении запроса: {response.status_code}')