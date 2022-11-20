class Rectangle:
    def __init__(self, width: float or int, height: float or int) -> None:
        self._height = height
        self._width = width

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, new_width) -> None:
        self._width = new_width
    
    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, new_height) -> None:
        self._height = new_height

    @property
    def area(self) -> float or int:
        return self._width * self._height

    def __str__(self) -> str:
        return f"Width: {self._width}\nHeight: {self._height}\nArea: {self.area}"


def use_it(rc: Rectangle):
    w = rc.width
    rc.height = 10
    expected = w * 10
    print(f"Expected an area of {expected}, but got {rc.area}")

if __name__ == "__main__":
    rect1 = Rectangle(10, 2.5)
    use_it(rect1)