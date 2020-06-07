def networkDelayTime(times, N,  K) -> int:
    times.sort(key=lambda x: x[0])
    positon = {}
    for i in range(len(times)):
        if times[i][0] not in positon:
            positon[times[i][0]] = i
    final_cost = {K: 0}
    cost = {}
    node = K
    while True:
        if node in positon:
            ps = positon[node]
            while ps < len(times) and times[ps][0] is node:
                if times[ps][1] in final_cost:
                    ps += 1
                    continue
                if times[ps][1] in cost:
                    cost[times[ps][1]] = min(cost[times[ps][1]], final_cost[node] + times[ps][2])
                else:
                    cost[times[ps][1]] = final_cost[node] + times[ps][2]
                ps += 1
        if len(cost) is 0:
            break
        least = min(cost.items(), key=lambda k: k[1])
        final_cost[least[0]] = least[1]

        node = least[0]
        del cost[least[0]]

    if len(final_cost) == N:
        return max(final_cost.items(), key=lambda k: k[1])[1]
    return False

times = [[1,2,1]]
N = 2
K = 2
print(networkDelayTime(times, N, K))
