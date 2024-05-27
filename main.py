from params import params_SPb, params_All
from utils import get_all_vacancies, vacancy_ids, response_vacancies
from blacklist import blacklist_vacancies, add_blacklist


def main():
    data = get_all_vacancies(params_SPb)
    b_list = blacklist_vacancies(data)
    add_blacklist(b_list)
    vacancy_l = vacancy_ids(data)
    response_vacancies(vacancy_l)
    data2 = get_all_vacancies(params_All)
    b_list2 = blacklist_vacancies(data2)
    add_blacklist(b_list2)
    vacancy_l2 = vacancy_ids(data2)
    response_vacancies(vacancy_l2)


if __name__ == '__main__':
    main()
