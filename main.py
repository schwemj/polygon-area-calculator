
import shape_calculator

# example usage code
rect = shape_calculator.Rectangle(5, 4)
print(rect.get_area())
rect.set_width(6)
print(rect.get_perimeter())
print(rect.get_picture())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
sq.set_height(3)
print(sq.get_diagonal())
print(sq.get_picture())
print(sq)