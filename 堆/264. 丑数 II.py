def nthUglyNumber(self, n: int):
    num = [1]
    p = [0, 0, 0]
    p2, p3, p5 = p[0], p[1], p[2]
    while len(num) < n:
        min_list = [num[p[0]] * 2, num[p[1]] * 3, num[p[2]] * 5]
        min_num, min_index = min(min_list), min_list.index(min(min_list))
        if num[-1] != min_num:
            num.append(min_num)
        p[min_index] += 1
        # print(p)
        # print(num)
    return num[n - 1]