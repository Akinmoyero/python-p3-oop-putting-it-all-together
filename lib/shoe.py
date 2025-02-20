class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string")
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")  # 🔹 Fix: Lowercase "size" to match test expectation
            return  # Prevents assignment of an invalid value
        if value <= 0:
            raise ValueError("Size must be greater than zero")
        self._size = value

    def cobble(self):
        self.condition = "New"  
        print("Your shoe is as good as new!")
