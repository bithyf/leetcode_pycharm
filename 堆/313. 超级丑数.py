def nthSuperUglyNumber(n: int, primes) -> int:
    p = [0] * len(primes)
    SuperUgly = [1]
    while len(SuperUgly) < n:
        uglylist = [SuperUgly[p[i]] * primes[i] for i in len(primes)]
        minugly ,min_index = min(uglylist), uglylist.index(min(uglylist))
        if minugly > SuperUgly[-1]:
            SuperUgly.append(minugly)
        p[min_index] += 1
    return SuperUgly[-1]