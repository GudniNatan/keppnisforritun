from random import randint


def heiltala(c):
    if '0' <= c <= '9':
        return int(c)
    return ord(c) - 87


def stafur(c):
    if 0 <= c <= 9:
        return str(c)
    return chr(87 + c)


def leggjaSaman(a, b):
    carry = 0
    s = ''
    for at in range(31, -1, -1):
        carry += heiltala(a[at]) + heiltala(b[at])
        s = stafur(carry % 16) + s
        carry = carry // 16
    return s


def brengla(s, at):
    magic = 'b058592efd277ae75f27bd99d1628fbd'
    if at >= len(s):
        return magic

    res = leggjaSaman(brengla(s, at+1), brengla(s, at+1))
    for i in range(6):
        res = leggjaSaman(res, res)
    

    cnt = ord(s[at])
    for i in range(cnt):
        res = leggjaSaman(res, magic)

    return res


def taetaLykilord(s):
    return brengla(s, 0)


def aftaeta(s):
    pass


for i in range(1000):
    assert heiltala(stafur(i)) == i


def taka_sundur(s):
    a = ""
    b = ""


# print(taetaLykilord('forrit123'))
print(taetaLykilord('abc'))

print(heiltala("3"))
print(heiltala("A"))
print(heiltala("B"))
magic = 'b058592efd277ae75f27bd99d1628fbd'
init = leggjaSaman(magic, magic)
loop = set()
for i in range(1000):
    magic = leggjaSaman(magic, magic)
    print(magic)
    if magic in loop:
        print(i)
        break
    loop.add(magic)
