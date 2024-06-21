'''
Filename: i.py
Author: Ethan Lemieux
Purpose: Demonstrate the Interface Segregation Principle (ISP)

'''

# base classes

class Catalogue:
    def add_to_catalogue(self):
        raise NotImplementedError
    
    def remove_from_catalogue(self):
        raise NotImplementedError
    
class Search:
    def search_by_title(self):
        raise NotImplementedError
    
    def search_by_author(self):
        raise NotImplementedError
    
    def search_by_genre(self):
        raise NotImplementedError
    
class Borrow:
    def borrow_book(self):
        raise NotImplementedError
    
    def return_book(self):
        raise NotImplementedError
    
class Report:
    def generate_report_borrowings(self):
        raise NotImplementedError
    
    def generate_report_overdue(self):
        raise NotImplementedError
    
    def generate_report_popularity(self):
        raise NotImplementedError

# people able to use base classes

class Librarian(Catalogue, Search, Borrow, Report):
    # implement capabilities
    ...
    
class User(Search, Borrow):
    # impliment capabilities
    ...

# base functionality. Some functions ommited because they are shared, and do not demonstrate ISP

def add_to_catelogue(person, title, author, genre):
    if isinstance(person, Librarian):
        person.add_to_catalogue(title, author, genre)

def remove_from_catelogue(person, title, author, genre):
    if isinstance(person, Librarian):
        person.remove_from_catalogue(title, author, genre)

def report_borrowings(person, material):
    if isinstance(person, Librarian):
        person.generate_report_borrowings

def report_overdue(person, material):
    if isinstance(person, Librarian):
        person.generate_report_overdue

def report_popularity(person, material):
    if isinstance(person, Librarian):
        person.generate_report_popularity