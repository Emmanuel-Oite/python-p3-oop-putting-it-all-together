# lib/shoe.py
class Shoe:
    def __init__(self, brand, size, color):
        self._brand = brand
        self._size = size
        self._color = color
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if not isinstance(brand, str) or len(brand) < 1 or len(brand) > 100:
            raise ValueError("Brand must be a string with a length between 1 and 100 characters")
        self._brand = brand
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if not isinstance(size, float) or size < 0 or size > 30:
            raise ValueError("Size must be a float between 0 and 30")
        self._size = size
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if not isinstance(color, str) or len(color) < 1 or len(color) > 100:
            raise ValueError("Color must be a string with a length between 1 and 100 characters")
        self._color = color