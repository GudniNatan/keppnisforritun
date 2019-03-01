from sys import stdin, stdout


class Person():
    def __init__(self, name, terms=None):
        self.name = name
        self.greater_than = set()
        self.in_degree = 0
        

def main():
    input = stdin.readline
    n, m = map(int, input().split())
    names = input().split()
    people = {name: Person(name) for name in names}
    heads = set(people)
    for _ in range(m):
        name1, op, name2 = input().split()
        if op == ">":
            name1, name2 = name2, name1
        people[name1].greater_than.add(name2)
        people[name2].in_degree += 1
        heads.discard(name2)
    if len(heads) != 1:
        print("veit ekki")
        return
    last = real = None
    current = people[list(heads)[0]]
    complete = [current.name]
    for _ in range(len(people)):
        if last == current or real != last:
            print("veit ekki")
            return
        real = current
        for name in real.greater_than:
            p = people[name]
            p.in_degree -= 1
            if p.in_degree == 0:
                last, current = current, p
                complete.append(name)
    print(*complete)


main()
