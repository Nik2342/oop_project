from src.hh import HeadHunterAPI
from src.js import JSONSaver
from src.user_interaction import user_interaction
from src.vacancy import Vacancy

hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies("Python")
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/123456", "0-10000", "Требования: опыт работы от 3 лет...")
json_saver = JSONSaver("vacancy.json")
json_saver.add_vacancy(hh_vacancies)
# json_saver.delete_vacancy("vacancy.json")

print(user_interaction(hh_vacancies))
