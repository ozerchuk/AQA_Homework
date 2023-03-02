# Task 1
class Point:
    x = None
    y = None

    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord


@property
def x_coord(self):
    return self._x_coord


@x_coord.setter
def x_coord(self, value):
    if not isinstance(value, (int, float)):
        raise TypeError
    self._x_coord = value


@property
def y_coord(self):
    return self._y_coord


@y_coord.setter
def y_coord(self, value):
    if not isinstance(value, (int, float)):
        raise TypeError
    self._y_coord = value


point1 = Point(5, 28)
print(point1.x_coord)
print(point1.y_coord)

point1.x_coord = 22
point1.y_coord = 'not a num'  # raise TypeError

print(point1.x_coord)  # output 3
print(point1.y_coord)  # output 2 (value hasn't changed due to an error)


# Task 2
class Line:
    begin = None
    end = None

    def __init__(self, begin_point, end_point):
        self.begin = begin_point
        self.end = end_point

    def length(self):
        x1, y1 = self.begin
        x2, y2 = self.end
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.length() == other.length()

    def __ne__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.length() != other.length()

    def __ge__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.length() >= other.length()

    def __le__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.length() <= other.length()

    def __gt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.length() > other.length()

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.length() < other.length()


line1 = Line((12, 6), (5, 6))
line2 = Line((0, 0), (5, 12))

# compare the lines by length
print(f'Line 1 ({line1.length()} units) == Line 2 ({line2.length()} units): {line1 == line2}')
print(f'Line 1 ({line1.length()} units) != Line 2 ({line2.length()} units): {line1 != line2}')
print(f'Line 1 ({line1.length()} units) >= Line 2 ({line2.length()} units): {line1 >= line2}')
print(f'Line 1 ({line1.length()} units) <= Line 2 ({line2.length()} units): {line1 <= line2}')
print(f'Line 1 ({line1.length()} units) > Line 2 ({line2.length()} units): {line1 > line2}')
print(f'Line 1 ({line1.length()} units) < Line 2 ({line2.length()} units): {line1 < line2}')
