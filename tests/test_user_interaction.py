import pytest

from src.user_interaction import (filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies,
                                  sort_vacancies, get_salary)

test_list = [
    {"name": "Программист", "salary": {"from": 10, "to": 20}},
    {"name": "Разработчик", "salary": {"from": 10, "to": 30}},
    {"name": "Тестировщик", "salary": {"from": 0, "to": 20}},
]


def test_filter_vacancies():
    result = filter_vacancies(test_list, ["Программист"])
    assert result == [{"name": "Программист", "salary": {"from": 10, "to": 20}}]

def test_get_salary():
    with pytest.raises(Exception) as ex:
        result = get_salary([
    {"name": "Программист", "salary": {"from": None, "to": None}},
    {"name": "Разработчик", "salary": {"from": 10, "to": 30}},
    {"name": "Тестировщик", "salary": {"from": 0, "to": 20}},
])



def test_empty_filter_vacancies():
    result = filter_vacancies(test_list, [])
    assert result == []

def test_get_vacancies_by_salary():
    result = get_vacancies_by_salary(test_list, "10-20")
    assert result == [{'name': 'Программист', 'salary': {'from': 10, 'to': 20}},
 {'name': 'Тестировщик', 'salary': {'from': 0, 'to': 20}}]

def test_wrong_get_vacancies_by_salary():
    result = get_vacancies_by_salary([
    {"name": "Программист", "salary": {"from": None, "to": None}},
    {"name": "Разработчик", "salary": {"from": 10, "to": 30}},
    {"name": "Тестировщик", "salary": {"from": 0, "to": 20}},
], "10-20")

def test_sort_vacancies():
    result = sort_vacancies(test_list)
    assert result == [{'name': 'Разработчик', 'salary': {'from': 10, 'to': 30}},
    {'name': 'Программист', 'salary': {'from': 10, 'to': 20}},
    {'name': 'Тестировщик', 'salary': {'from': 0, 'to': 20}}]

def test_get_top_vacancies():
    result = get_top_vacancies(test_list, 2)
    assert result == [
        {'name': 'Программист', 'salary': {'from': 10, 'to': 20}},
        {'name': 'Разработчик', 'salary': {'from': 10, 'to': 30}}]


def test_print_vacancies():
    result = print_vacancies(test_list)
    assert result == None
