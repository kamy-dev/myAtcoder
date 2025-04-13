def main():
    n = int(input())
    A = [int(i) for i in input().split()]

    flag = 1
    cnt = 0

    while flag:
        flag = 0
        for i in range(n-1, 0, -1):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                flag = 1
                cnt += 1
    print(*A)
    print(cnt)
    return

if __name__ == '__main__':
    main()