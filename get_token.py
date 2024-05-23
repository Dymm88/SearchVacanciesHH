import requests

from config import (CLIENT_ID, CLIENT_SECRET,
                    REDIRECT_URI, TOKEN, REFRESH_TOKEN)


def get_code():
    auth_code = (f'https://hh.ru/oauth/authorize?'
                 f'response_type=code&client_id={CLIENT_ID}&'
                 f'redirect_uri={REDIRECT_URI}')
    print('Перейди по ссылке и скопируй код:', auth_code)
    code = input('Вставь код авторизации: ')
    return code


def get_token(ac_code):
    url = 'https://api.hh.ru/token'
    headers = {
        'Usr-Agent': 'VacancyBot',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': ac_code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI,
    }
    r = requests.post(url=url, headers=headers, data=data)
    print(r.json())


def refresh_token():
    url = 'https://api.hh.ru/token'
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'User-Agent': 'VacancyBot',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': REFRESH_TOKEN,
    }
    r = requests.post(url=url, headers=headers, data=data)
    print(r.json())


""" Ненужное закомментировать """
if __name__ == '__main__':
    """ Для получения токена """
    access_code = get_code()
    get_token(access_code)
    """ Для обновления токена """
    refresh_token()
