import requests

from config import HEADERS, RESUME
from message import MESSAGE_TEXT


def get_all_vacancies(params: dict[str | int | bool]) -> list[dict]:
    url = "https://api.hh.ru/vacancies"

    vacancy_list = []
    while True:
        r = requests.get(url=url, headers=HEADERS, params=params)
        items = r.json()["items"]
        vacancy_list += items
        if r.json()["pages"] == params["page"] + 1:
            break
        params["page"] += 1
    return vacancy_list


def vacancy_ids(list_data: list[dict]) -> list[int]:
    vacancy_id = [vacancy["id"] for vacancy in list_data]
    return vacancy_id


def response_vacancies(list_vacancies: list[int]):
    success = 0
    for item in list_vacancies:
        r = requests.post(
            f"https://api.hh.ru/negotiations?resume_id={RESUME}&vacancy_id={str(item)}&message={MESSAGE_TEXT}",
            headers=HEADERS,
        )
        if r.status_code == 201:
            success += 1
            print(f"Резюме успешно отправлено на вакансию {item}")
        else:
            print(f"Произошла ошибка при отправке на вакансию {item}: {r.status_code}")
    print(f"Количество отправленных отзывов - {success}")
