




q=  [1,2,3,4,5]
def te():
    while q:
        qa = q.pop()
        for _ in range(10):
            if qa == 2:
                return 0
            else:
                print(qa)
te()
