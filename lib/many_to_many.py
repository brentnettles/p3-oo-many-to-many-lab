class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)        

    def contracts(self): #This method should return a list of related contracts.
        return [contract for contract in Contract.all if contract.author == self]


    def books(self):# This method should return a list of related books using the Contract class as an intermediary.
        return [contract.book for contract in self.contracts()] # <-- passing to function in Contracts

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

#    ''' 
#     def total_royalties(self):
        
#         royalties_list = []

#         for contract in self.contracts():
#             royalties_list.append(contract.royalties)

#         total_royalties = sum(royalties_list)
    
#         return total_royalties
    
#     def total_royalties(self):
#         return sum([contract.royalties for contract in self.contracts()])
#     '''

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    #iterates over each contract object returnef by the self.contracts()
    #sum() is the method with the [] as the variable 
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contract()]) 
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    
    def __repr__(self):
        return f"Author('{self.name}')"

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        # self.author = author
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]
    
    # def contracts(self):
    #     contracted_books = []
    #     for contract in Contract.all:
    #         if contract.book is self:
    #             contracted_books.append(contract)
    #     return contracted_books
    
    def authors(self):
        return [contract.author for contract in self.contracts()]

    def __repr__(self):
        return f"Book('{self.title}')"

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.date = date
        self.book = book
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        contracts_on_date = []
        for contract in cls.all:
            if contract.date == date:
                contracts_on_date.append(contract)
        return contracts_on_date

    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    @property 
    def book(self):
        return self._book 
    
    @book.setter 
    def book(self,value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception
        self._date = value

    @property
    def royalties(self):
        return self._royalties 
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception
        self._royalties = value

    def __repr__(self):
        return f"Contract({self.author}, {self.book}, '{self.date}', {self.royalties})"
 
author1 = Author("Mo")
author2 = Author("Mike")
author2 = Author("Mike")
author2 = Author("Mike")
author2 = Author("Mike")
author2 = Author("Mike")

# Creating books
book1 = Book("The Mo story")
book2 = Book("I wanna be like Mike")

# Creating contracts
contract1 = Contract(author1, book1, "2024", 420)
contract2 = Contract(author2, book2, "2024-03-18", 69)
contract3 = Contract(author1, book2, "2024-03-19", 666)

# Signing contracts
author1.sign_contract(book1, "2024-03-20", 1200)
author2.sign_contract(book1, "2024-03-21", 1800)
author2.sign_contract(book2, "2024-03-22", 2200)

print(Author.all)
print(Book.all)
