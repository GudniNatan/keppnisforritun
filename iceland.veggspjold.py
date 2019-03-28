class Poster(object):
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def collides(self, other):
        return (self.x2 > other.x1 and self.y2 > other.y1 and
                self.x1 < other.x2 and self.y1 < other.y2)
        

    def calculateArea(self):
        return self.x2 - self.x1 * self.y2 - self.y1


b, h, n = map(int, input().split())

posters = list()
for i in range(n):
    posters.append(list(map(int, input().split())))

posters.sort()
print(posters)
