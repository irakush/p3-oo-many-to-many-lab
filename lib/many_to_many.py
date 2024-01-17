import ipdb


class Author:
    all = []  # class variable

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [
            contract for contract in Contract.all if contract.author == self
        ]  # list comprehesion

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([each.royalties for each in self.contracts()])


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise Exception

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = value
        else:
            raise Exception

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if isinstance(value, int):
            self._royalties = value
        else:
            raise Exception

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]


# b1 = Book("Book #1")
# a1 = Author("Author #1")
# c1 = Contract(a1, b1, "Monday", 20)

# b2 = Book("Book #2")
# a2 = Author("Author #2")
# c2 = Contract(a2, b2, "Tuesday", 50)

# c3 = Contract(a1, b1, "Monday", 70)
# c4 = Contract(a1, b1, "Monday", 10)

# ipdb.set_trace()
