def reconstructQueue(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    key = []
    for p in people:
        key.insert(p[1], p[0])
    return key