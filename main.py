from params import params_SPb, params_All
from utils import get_all_vacancies, vacancy_ids, response_vacancies

if __name__ == "__main__":
    data = get_all_vacancies(params_SPb)
    vacancy_l = vacancy_ids(data)
    response_vacancies(vacancy_l)
    data2 = get_all_vacancies(params_All)
    vacancy_l2 = vacancy_ids(data2)
    response_vacancies(vacancy_l2)
