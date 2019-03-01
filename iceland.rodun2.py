from dataclasses import dataclass, field
from queue import PriorityQueue


@dataclass(order=True)
class Person:
    name: str = field(compare=False)
    priority: int = 0
    greater_than: set = field(default_factory=set, compare=False)


def main():
    n, m = map(int, input().split())
    names = input().split()
    people = {name: Person(name) for name in names}


a = PriorityQueue()
a._put(Person("jon", 0))
a._put(Person("jona", 2))
a._put(Person("helgi", 6))
a._put(Person("bardur", 3))
print(a._get().name)
print(a._get().name)
print(a._get().name)
print(a._get().name)
