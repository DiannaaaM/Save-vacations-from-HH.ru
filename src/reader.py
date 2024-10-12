import json
from typing import Any


class ReadWriteFiles:
    """
    Класс для работы с файлами
    """

    def __init__(self, content: Any) -> None:
        self.file_path = "../data/Vacantions.json"
        self.content = content

    def write_to_file(self) -> None:
        with open(self.file_path, "w", encoding="utf8") as file:
            json.dump(self.content, file, indent=4, ensure_ascii=False)

    def read_from_file(self) -> None:
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()
