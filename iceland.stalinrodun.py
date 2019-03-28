# super naive

n = int(input())
my_list = list(map(int, input().split()))
k = 0
while my_list:
    k += 1
    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] > my_list[i - 1] or i == 0:
            my_list.pop(i)
print(k)
