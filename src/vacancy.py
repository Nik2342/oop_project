class Vacancy:

    __slots__ = ("name", "url", "salary", "description")

    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = self._validate_salary(salary)
        self.description = description

    @staticmethod
    def _validate_salary(salary):
        try:
            if "-" in salary:
                min_salary, max_salary = salary.split("-")
                if int(max_salary.strip()) <= 0:
                    raise ValueError("Зарплата должна быть больше 0")
                return int(max_salary.strip())
            else:
                if int(salary.strip()) <= 0:
                    raise ValueError("Зарплата должна быть больше 0")
                return int(salary)
        except Exception as ex:
            print(ex)

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
