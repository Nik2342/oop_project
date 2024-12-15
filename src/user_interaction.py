def user_interaction(vacancies_list):
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


def filter_vacancies(vacancies_list: list, filter_words: list) -> list:
    result = []
    for vacancy in vacancies_list:
        for word in filter_words:
            if word.lower() == vacancy.get("name").lower():
                result.append(vacancy)
    return result


def get_vacancies_by_salary(vacancies_list: list, salary_range: str) -> list:
    min_salary=0
    max_salary= 0
    try:
        min_salary_str, max_salary_str = salary_range.split("-")
        min_salary = int(min_salary_str)
        max_salary = int(max_salary_str)
    except Exception as ex:
        print("Неверный формат записи диапазона\n Пример 0-10000")
    result = []
    vacancy_salary = 0
    try:
        for vacancy in vacancies_list:
            if vacancy.get("salary").get("to") is None:
                if vacancy.get("salary").get("from") is None:
                    raise Exception
                else:
                    vacancy_salary = vacancy.get("salary").get("from")
            else:
                vacancy_salary = vacancy.get("salary").get("to")

            if min_salary <= vacancy_salary <= max_salary:
                result.append(vacancy)
    except Exception as ex:
        print(ex)

    return result


def get_salary(vacancies_list: list) -> list:
    vacancy_salary = 0
    for vacancy in vacancies_list:
        if vacancy.get("salary").get("to") is None:
            if vacancy.get("salary").get("from") is None:
                raise Exception
            else:
                vacancy_salary = vacancy.get("salary").get("from")
        else:
            vacancy_salary = vacancy.get("salary").get("to")
    return vacancy_salary


def sort_vacancies(vacancies_list: list) -> list:
    return sorted(vacancies_list, key=lambda vacancy: get_salary([vacancy]), reverse=True)


def get_top_vacancies(vacancies_list: list, amount: int) -> list:
    return vacancies_list[:amount]


def print_vacancies(vacancies_list: list) -> list:
    for vacancy in vacancies_list:
        print(vacancy)
