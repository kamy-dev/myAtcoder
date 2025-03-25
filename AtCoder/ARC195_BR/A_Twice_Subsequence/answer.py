def Solution():
    N, M = map(int, input().split())
    A = [int(x) for x in input().split(" ")]
    B = [int(x) for x in input().split()]

    # 変数ansを用意して、数列Aに部分列Bがあった場合にインクリメントするカウンターを定義
    ans = 0

    #数列A内に部分列Bが存在した際のindexを保持するリストを定義
    ans1 = [-1]*M
    ans2 = [-1]*M

    # 走査する中で部分列Bのインデックスを保持するカウンタを定義
    idx1 = 0
    idx2 = M-1

    # 前から走査するforループ
    for i in range(N):
        if A[i] == B[idx1]:
            ans1[idx1] = i
            idx1 += 1
        if idx1 == M:
            ans += 1
            break
    
    # 後ろから走査するforループ
    for i in range(N-1, -1, -1):
        if A[i] == B[idx2]:
            ans2[idx2] = i
            idx2 -= 1
        if idx2 == -1:
            ans += 1
            break

    # ans1とans2が異なればYes、それ以外はNo
    if  ans >= 2 and ans1 != ans2:
        print("Yes")
    else:
        print("No")

Solution()