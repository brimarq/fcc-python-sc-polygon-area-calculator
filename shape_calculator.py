class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        # diagonal = sqrt of (width squared + height squared)
        return ((self.width ** 2) + (self.height ** 2)) ** (1/2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ''
        for line in range(self.height):
            picture += "*" * self.width + "\n"
        
        return picture

    def get_amount_inside(self, shape):
        num_widths = self.width // shape.width
        num_heights = self.height // shape.height
        return num_widths * num_heights

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"



class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.height})"
