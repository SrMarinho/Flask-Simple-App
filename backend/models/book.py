import json
import time
import random

class Book:
    def __init__(self, id:int, title:str, author:str, rented:bool):
        self.id = id
        self.title = title
        self.author = author
        self.rented = rented

    @staticmethod
    def getBooks():
        for i in range(10):
            yield Book(i + 1, "Livro " + str(i), "Autor " + str(i), False)
            time.sleep(random.random() * 0.5)


    def toJson(self) -> str:
        return json.dumps(self.toDict())

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "rented": self.rented
        }