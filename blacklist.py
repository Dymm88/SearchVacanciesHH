import requests
from params import params_SPb, params_All
from config import HEADERS


def get_all_vacancies(params: dict[str | int | bool]) -> list[dict]:
    url = 'https://api.hh.ru/vacancies'

    vacancy_list = []
    while True:
        r = requests.get(url=url, headers=HEADERS, params=params)
        items = r.json()['items']
        vacancy_list += items
        if r.json()['pages'] == params['page'] + 1:
            break
        params['page'] += 1
    return vacancy_list


def blacklist_vacancies(list_vacancies):
    company_name = (
        'Aston',
        'Яндекс Крауд',
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


if __name__ == '__main__':
    data = get_all_vacancies(params_SPb)
    b_list = blacklist_vacancies(data)
    add_blacklist(b_list)
    data1 = get_all_vacancies(params_All)
    b_list2 = blacklist_vacancies(data1)
    add_blacklist(b_list2)
