from enum import Enum
from abc import abstractclassmethod

class Relationship(Enum):
    PARENT = "parent"
    CHILD = "child"
    SIBLING = "sibling"


class Person:
    def __init__(self, name: str) -> None:
        self.name = name


class RelationshipBrowser:
    @abstractclassmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):
    def __init__(self) -> None:
        self.relations = []
    
    def add_parent_and_child(self, parent: Person, child: Person):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )

        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name: str):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    def __init__(self, browser: RelationshipBrowser) -> None:
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")

parent1 = Person("John")
child1 = Person("Neymar")
child2 = Person("Vampeta")

relations = Relationships()
relations.add_parent_and_child(parent1, child1)
relations.add_parent_and_child(parent1, child2)

Research(relations)
