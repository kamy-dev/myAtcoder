def main():
    n = int(input())
    SB = input().split()
    SS = SB.copy()

    # Bubble Sortで数字を基準に昇順にソートする
    for i in range(n):
        for j in range(n-1, i, -1):
            if int(SB[j][1]) < int(SB[j-1][1]):
                SB[j], SB[j-1] = SB[j-1], SB[j]
    print(*SB)
    print("Stable")

    # Selection Sortで数字を基準に昇順にソートする
    for i in range(n):
        minj = i
        for j in range(i, n):
            if int(SS[j][1]) < int(SS[minj][1]):
                minj = j
        SS[i], SS[minj] = SS[minj], SS[i]

    print(*SS)
    if SS == SB:
        print("Stable")
    else:
        print("Not stable")

    return

if __name__ == '__main__':
    main()