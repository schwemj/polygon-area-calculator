
class Rectangle():

    def __init__(self, w, h):
        self.width = w  # set initial width
        self.height = h  # set initial height

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):  # print picture of shape
        self.shape = '*' * self.width + '\n'
        if len(self.shape) < 50 and self.height < 50:  # enforcing size limit of 50*50
            picture = self.shape * self.height
            return picture
        else:
            return 'Too big for picture.'

    def get_amount_inside(self, other):
        h_fit = self.width // other.width  # how many shapes fit horizontally
        v_fit = self.height // other.height  # how many shapes fit vertically
        return h_fit * v_fit

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side_length):  # overrides method in Rectangle class
        self.width = side_length  # set initial width
        self.height = side_length  # set initial height

    def set_side(self, side_length):  # adjusts both sides at once
        self.width = side_length
        self.height = side_length

    def set_width(self, w):  # overrides method in Rectangle class
        self.set_side(w)

    def set_height(self, h):  # overrides method in Rectangle class
        self.set_side(h)  # same as set_width method

    def __str__(self):
        return f'Square(side={self.width})'
