def travel(p):
    if p.left:
        print(p.val)
        t = p.right
        p.right = p.left
        p.left = None
        p = p.right
        print(p.val)
        print("------")
        p = travel(p)

        print("tavel")
        print(p)
        print('.....')
        p.right = t
        print(p)
        print(',,,,,,,')
    if p.right:
        p = p.right
        p = travel(p)
    return p
