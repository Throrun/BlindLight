class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Coordinates):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Coordinates({self.x}, {self.y})"
    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def move_x(self, number: int) -> None:
        self.x += number

    def move_y(self, number: int) -> None:
        self.y += number
