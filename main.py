from src.hh import HH
from src.readers import Readers
from src.vacancies import Vacancies




if __name__ == "__main__":
    user_vacancies = input("Какая вакансия интересует?\n")
    user_top = input("Сколько подобранных вакансий в конце ты хотел бы увидеть?\n")
    user_key = input("Which key would you like tofind in vacancions?\n")
    hh_response = HH(user_vacancies)
    vacancies_response = Vacancies(hh_response, user_top, user_key)
    print(f"Итоговый список вакансий:\n {vacancies_response.sort_vacancies_by_salary()}")
    print("Больше вакансий в файле - 'Vacantions.json'")
    reader = Readers(vacancies_response)
