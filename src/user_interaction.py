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


def filter_vacancies(vacancies_list, filter_words):
    result = []
    for vacancy in vacancies_list:
        for word in filter_words:
            if word.lower() == vacancy.get("name").lower():
                result.append(vacancy)
    return result


def get_vacancies_by_salary(vacancies_list, salary_range):
    try:
        min_salary, max_salary = salary_range.split("-")
        min_salary = int(min_salary)
        max_salary = int(max_salary)
    except Exception as ex:
        print("Неверный формат записи диапазона\n Пример 0-10000")
    result = []
    for vacancy in vacancies_list:
        if min_salary <= vacancy.salary <= max_salary:
            result.append(vacancy)
    return result


def sort_vacancies(vacancies_list):
    return sorted(vacancies_list, key=lambda vacancy: vacancy.max_salary, reverse=True)


def get_top_vacancies(vacancies_list, amount):
    return vacancies_list[:amount]


def print_vacancies(vacancies_list):
    for vacancy in vacancies_list:
        print(vacancy)
