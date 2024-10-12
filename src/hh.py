from abc import ABC, abstractmethod
from typing import Any

import requests


class Parser(ABC):
    """
    Абстрактный базовый класс для парсинга вакансий
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, keyword: Any) -> None:
        self.keyword = keyword
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "text": self.keyword,
            "per_page": 30,
        }
        self.end_vacancies = []

    def load_vacancies(self) -> list:
        """
        Загрузка вакансий с помощью API HeadHunter
        """
        response = requests.get(self.url, params=self.params)
        try:
            data = response.json()
            vacancies = data.get("items", [])
            self.end_vacancies.append(vacancies)
        except response.status_code != 200:
            print("Что-то пошло не так:(")
        finally:
            return self.end_vacancies
