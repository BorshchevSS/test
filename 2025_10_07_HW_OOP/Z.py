"""Задание: «Система управления библиотекой»
Описание
Необходимо смоделировать простую систему учёта книг в библиотеке с использованием классов и наследования.
Требования:
1. Создайте базовый класс Item, который будет описывать общий объект в библиотеке.
    ◦ Атрибуты:
        ▪ title (название)
        ▪ year (год издания)
    ◦ Метод __str__() для красивого вывода информации.
2. Создайте класс-наследник Book, расширяющий функциональность:
    ◦ Дополнительные атрибуты:
        ▪ author (автор)
        ▪ pages (количество страниц)
    ◦ Переопределите метод __str__(), чтобы он включал все атрибуты.
3. Создайте ещё один класс-наследник Magazine:
    ◦ Дополнительные атрибуты:
        ▪ issue (номер выпуска)
        ▪ publisher (издательство)
    ◦ Переопределите метод __str__()."""


#Элемент
class Item:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"Название: '{self.title}'; Год издания: {self.year}"

x = Item("test", 2012)
print(x)


class Book(Item):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Название: '{self.title}'; Год издания: {self.year}; Автор: {self.author}; Количество страниц: {self.pages}"

print(Book("test2", 2025, "Tom Soer", 123))


class Magazine(Book):
    def __init__(self, title, year, author, pages, issue, publisher):
        super().__init__(title=title, year=year, author=author, pages=pages)
        self.issue = issue
        self.publisher = publisher

    def __str__(self):
        return f"Название: '{self.title}'; Год издания: {self.year}; Автор: {self.author}; Количество страниц: {self.pages}; номер выпуска: {self.issue}; Издательство: {self.publisher}"

print(Magazine("test3", 2030, "BSS", 777, 4, "msk"))