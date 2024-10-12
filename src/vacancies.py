from typing import Any

from src.hh import HH


class Vacancies:
    """
    Класс для обработки списка вакансий
    """

    # __slots__ = ('vacantions_list')

    def __init__(self, vacancies_list: Any, top: Any, keywords: Any) -> None:
        self.vacancies_list = vacancies_list
        self.top = top
        self.keywords = keywords
        self.processed_vacancies = []
        self.sorted_vavantions = []

    def processing_vacancies(self) -> list:
        """
        Метод для обработки списка вакансий
        """
        for vacancy in self.vacancies_list:
            for v in vacancy:
                if "snippet" in v and "requirements" in v["snippet"] and self.keywords in v["snippet"]["requirements"]:
                    processed_vacancy = {
                        "ID": v["id"],
                        "Title": v["name"],
                        "Salary from": v["salary"]["from"] if v["salary"] and "from" in v["salary"] else 0,
                        "Salary to": v["salary"]["to"] if v["salary"] and "to" in v["salary"] else 0,
                        "Company": v["employer"]["name"],
                        "URL": v["url"],
                        "Description": v["snippet"]["requirement"],
                    }
                    self.processed_vacancies.append(processed_vacancy)
        return self.processed_vacancies

    def sort_vacancies_by_salary(self):
        """
        Метод для сортировки вакансий по зарплате
        """
        self.sorted_vacancies = sorted(
            self.processed_vacancies,
            key=lambda x: (x["Salary from"] if x["Salary from"] is not None else float("-inf")),
            reverse=True,
        )
        return self.sorted_vacancies[: self.top]


hh = HH("Python developer")
a = hh.load_vacancies()
# print(a)
for i in a:
    for q in i:
        print(q)
        print()
v = Vacancies(a, 2, "Python")
x = v.processing_vacancies()
print(x)
# print(v.sort_vacancies_by_salary())
