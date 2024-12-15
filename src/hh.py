from abc import ABC, abstractmethod

import requests


class VacanciesApi(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(VacanciesApi):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self._url = "https://api.hh.ru/vacancies"
        self._headers = {"User-Agent": "HH-User-Agent"}
        self._params = {"text": "", "page": 0, "per_page": 100}
        self._vacancies = []

    def get_vacancies(self, keyword):
        self._params["text"] = keyword
        while self._params.get("page") != 20:
            response = requests.get(self._url, headers=self._headers, params=self._params)
            vacancies = response.json()["items"]
            self._vacancies.extend(vacancies)
            self._params["page"] += 1
        return self._vacancies
