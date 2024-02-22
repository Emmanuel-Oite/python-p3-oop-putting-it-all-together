# lib/book.py
class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str) or len(title) < 1 or len(title) > 100:
            raise ValueError("Title must be a string with a length between 1 and 100 characters")
        self._title = title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, str) or len(author) < 1 or len(author) > 100:
            raise ValueError("Author must be a string with a length between 1 and 100 characters")
        self._author = author
    
    @property
    def pages(self):
        return self._pages
    
    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Number of pages must be an integer greater than 0")
        self._pages = pages