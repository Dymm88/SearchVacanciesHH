import requests
from config import HEADERS


def blacklist_vacancies(list_vacancies):
    company_name = (
        'Aston',
        'Яндекс Крауд',
        'Яндекс Крауд: Поддержка',
        'Rebotica',
    )

    black_list = [vacancy for vacancy in list_vacancies
                  if vacancy['employer']['name'] in company_name]
    return black_list


def add_blacklist(company_list):
    for name in company_list:
        r = requests.put(url=f'https://api.hh.ru/vacancies/blacklisted/{str(name['id'])}',
                         headers=HEADERS)
        if r.status_code == 204:
            print(f'Вакансия {name['employer']['name']} добавлена в черный список')
        else:
            print(f'Произошла ошибка при добавлении в черный список: {r.status_code}')
