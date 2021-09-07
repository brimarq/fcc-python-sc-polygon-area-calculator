class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self):
        pass

    def set_height(self):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def get_diagonal(self):
        pass

    def get_picture(self):
        pass

    def get_amount_inside(self):
        pass

    def __str__(self):
        return f"Rectangle(width={self.width},height={self.height})"



class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def set_side(self):
        pass

    def set_width(self):
        pass

    def set_height(self):
        pass

    def __str__(self):
        return f"Square(side={self.height}"
