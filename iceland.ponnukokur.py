from sys import stdin, stdout


def print(msg):
    stdout.write(str(msg))
    stdout.write("\n")


def get_seg_sum(from_pos, to_pos, seg, seg_sum, seg_size):
    total = 0
    if to_pos - from_pos > seg_size // 2:
        for i in range(from_pos):
            total += seg[i]
        for i in range(to_pos, seg_size):
            total += seg[i]
        total = seg_sum - total
    else:
        for i in range(from_pos, to_pos + 1):
            total += seg[i]
    return total


input = stdin.readline
n, q = map(int, input().split())

seg_size = 150
segments = [[0 for _ in range(seg_size)] for _ in range(n // seg_size)]
segments.append([0 for _ in range(n % seg_size)])
reverse = False
seg_total = [0 for _ in range(n // seg_size + 1)]

for _ in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        i = cmd[1] - 1
        div, mod = divmod(i, seg_size)
        side = int(not segments[div][mod])
        seg_total[div] += 1 if side else -1
        segments[div][mod] = side
    elif cmd[0] == 2:
        reverse = not reverse
    elif cmd[0] == 3:
        if reverse:
            print(n - sum(seg_total))
        else:
            print(sum(seg_total))
    else:
        m, l, r = cmd
        total = 0
        l, r = l - 1, r - 1
        div, mod = divmod(l, seg_size)
        div2, mod2 = divmod(r, seg_size)
        if div == div2:
            total = get_seg_sum(
                mod, mod2, segments[div], seg_total[div], seg_size)
        else:
            total = get_seg_sum(
                mod, seg_size - 1, segments[div], seg_total[div], seg_size)
            total += get_seg_sum(
                0, mod2, segments[div2], seg_total[div2], seg_size)
            for i in range(div + 1, div2):
                total += seg_total[i]
        if reverse:
            total = r - l - total + 1
        print(total)
