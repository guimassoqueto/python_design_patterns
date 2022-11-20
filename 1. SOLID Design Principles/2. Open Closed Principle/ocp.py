from enum import Enum
from typing import List

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


class Size(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'


class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self) -> str:
        return f'{self.name}, {self.color.value}, {self.size.value}'


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items: List[Product], spec: Specification):
        pass


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args
    
    def is_satisfied(self, item: Product):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class ColorSpecification(Specification):
    def __init__(self, color: Color) -> None:
        self.color = color

    def is_satisfied(self, item: Product):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size: Size) -> None:
        self.size = size

    def is_satisfied(self, item: Product):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items: List[Product], spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.RED, Size.SMALL)
    green_apple = Product("Green Apple", Color.GREEN, Size.SMALL)
    pear = Product("Pear", Color.GREEN, Size.SMALL)

    items_list: List[Product] = [ apple, green_apple, pear ]

    better_filter = BetterFilter()
    small = SizeSpecification(Size.SMALL)

    for item in better_filter.filter(items_list, small):
        print(f"small item: {item.name}")

    small_and_green = small & ColorSpecification(Color.GREEN)
    for item in better_filter.filter(items_list, small_and_green):
        print(f"small and green: {item.name}")