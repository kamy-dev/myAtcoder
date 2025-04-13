def main():
    n = int(input())

    maxv = -10**18
    minv = 10**18

    for _ in range(n):
        r = int(input())
        maxv = max(maxv, r - minv)
        minv = min(minv, r)

    print(maxv)

    return 

if __name__ == '__main__':
    main()
