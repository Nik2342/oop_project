import json


class JSONSaver:

    def __init__(self):
        pass

    @staticmethod
    def add_vacancy(vacancy_list, file):
        result = []
        for vacancy in vacancy_list:
            with open(file, "a+", encoding="utf-8") as jsfile:
                js = json.dumps(vacancy)
                if js not in jsfile:
                    result.append(js)
                    jsfile.write(js)
                    jsfile.close()
                else:
                    continue

    @staticmethod
    def get_vacancies(file):
        with open(file, "r+", encoding="utf-8") as file:
            jsfile = file.read()
            return jsfile

    @staticmethod
    def delete_vacancy(file):
        with open(file, "r+", encoding="utf-8") as file:
            file.truncate(0)
