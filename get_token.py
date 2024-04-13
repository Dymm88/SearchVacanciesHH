import requests

from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, EMAIL, REFRESH_TOKEN


def get_access_code():
    url = 'https://hh.ru/oauth/autorize'
    authorize_url = url + '?response_type=code&client_id=' + CLIENT_ID + '&redirect_uri=' + REDIRECT_URI
    print('Переход на страницу авторизации: ', authorize_url)
    access_code = input('Код авторизации: ')
    return access_code


headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': f'VacancyBot/1.0 ({EMAIL})',
}

token_url = 'https://hh.ru/oauth/token'


def get_access_token(access_code):
    data = {
        'grand_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': access_code,
        'redirect_uri': REDIRECT_URI,
    }

    r = requests.post(token_url, headers=headers, data=data)
    token = r.json()['access_token']
    refresh = r.json()['refresh_token']
    print(token)
    print(refresh)


def refresh_token():
    data = {
        'grand_type': 'refresh_token',
        'refresh_token': REFRESH_TOKEN,
    }

    r = requests.post(token_url, headers=headers, data=data)
    token = r.json()['access_token']
    refresh = r.json()['refresh_token']
    print(token)
    print(refresh)


if __name__ == '__main__':
    refresh_token()
