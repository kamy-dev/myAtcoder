n = int(input())
d = {}
for i in range(n):
    opt, data = input().split()
    if opt == "insert":
        d[data] = True
    elif opt == "find":
        if data in d:
            print("yes")
        else:
            print("no")
