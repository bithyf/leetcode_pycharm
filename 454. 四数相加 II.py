def fourSumCount(A, B, C, D) -> int:
    sumAB = dict()
    for numa in A:
        for numb in B:
            if sumAB[numa + numb] in sumAB:
                sumAB[numb + numa] += 1
            else:
                sumAB[numa + numb] = 1
    count = 0
    for numc in C:
        for numd in d:
            if sumAB[-(numc + numd)] in sumAB:
                count += sumAB[-(numc + numd)]

    return count