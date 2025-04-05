N = int(input())
A = list(map(int, input().split()))

# リストAの全ての値が偶数であることを確認するカウンター
chk = 0
# 最大操作回数を保持するカウンター
cnt = 0


# 全て偶数か判定する。これは「黒板の整数全てを2で割る作業」の前に必ず繰り返す。
for i in range(N):
    if A[i] % 2 == 0:
        chk += 1