class Vacancy:
    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description
        if len(self.salary) == 0:
            raise ValueError("Зарплата должна быть больше 0")
        min_salary, max_salary = salary.split("-")
        self.salary = int(max_salary)

    @staticmethod
    def cast_to_object_list(vacancy_list):
        result = []
        for vacancy in vacancy_list:
            if vacancy.get("salary"):
                vacancy_add = {
                    "name": vacancy.get("name"),
                    "url": vacancy.get("url"),
                    "salary": vacancy.get("salary").get("from") or vacancy.get("salary").get("to"),
                    "description": vacancy.get("snippet").get("responsibility"),
                }
                result.append(vacancy_add)
            else:
                continue
        return result
