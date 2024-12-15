import json
from abc import ABC, abstractmethod


class Saver(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy_list):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver:

    def __init__(self, file):
        self.file = file

    def add_vacancy(self, vacancy_list):
        result = []
        for vacancy in vacancy_list:
            with open(self.file, "a+", encoding="utf-8") as jsfile:
                js = json.dumps(vacancy)
                if js not in jsfile:
                    result.append(js)
                    jsfile.write(js)
                    jsfile.close()
                else:
                    continue

    def get_vacancies(self):
        with open(self.file, "r+", encoding="utf-8") as file:
            jsfile = file.read()
            return jsfile

    def delete_vacancy(self):
        with open(self.file, "r+", encoding="utf-8") as file:
            file.truncate(0)
