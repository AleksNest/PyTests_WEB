import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# функция получения токена по логину и паролю
def get_login():
    path_1 = data.get('path_1')
    post = requests.post(url=path_1, data={'username': data.get('username'), 'password': data.get('password')})
    if post.status_code == 200:
        return post.json()['token']

# получение чужих постов по токену
def get_post_other(token):
    path_2 = data.get('path_2')
    get = requests.get(url=path_2, params={'owner': 'notMe'}, headers={'X-Auth-Token': token}) #получает чужие посты
    get = requests.get(url=path_2, headers={'X-Auth-Token': token})
    if get.status_code == 200:
        for item in get.json()['data']:
            print(item)
        return get.json()

# получение своих постов по токену
def get_post_own(token):
    path_2 = data.get('path_2')
    get = requests.get(url=path_2, headers={'X-Auth-Token': token})
    if get.status_code == 200:
        for item in get.json()['data']:
            print(item)
        return get.json()


# создание нового поста по токену
def create_post(token):
    username = data.get('username')
    password = data.get('password')
    path_2 = data.get('path_2')
    title = 'Заголовок новый 2'
    description = 'описание новое '
    content = 'контент новый'
    post = requests.post(url=path_2, headers={"X-Auth-Token": token}, params={
        'username': username,
        'password': password,
        'title': title,
        'description': description,
        'content': content})

    if post.status_code == 200:
        print(post.status_code)
        return post.json()['title']




if __name__ == '__main__':
    token = get_login()
    get_post_other(token)
    get_post_own(token)

