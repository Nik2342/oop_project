import pytest

from src.vacancy import Vacancy


def test_vacancy_name():
    vacancy = Vacancy("Разработчик", "test_url", "10-100", "Тестовая работа")
    assert vacancy.name == "Разработчик"


def test_salary():
    vacancy = Vacancy("Разработчик", "test_url", "10-100", "Тестовая работа")
    assert vacancy.salary == 100


def test_zero_salary():
    # with pytest.raises(ValueError) as exc_info:
    vacancy = Vacancy("Разработчик", "test_url", "0", "Тестовая работа")
    assert vacancy.salary == None
