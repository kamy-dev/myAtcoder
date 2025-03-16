import random

N, L = map(int, input().split())
T = map(int,input().split())

# 各社員の番号を初期化
a = list(range(N)) # 0, 1, 2, ..., N-1
b = [(i + 1) % N for i in range(N)]

# 実際の掃除回数リストと掃除当番の初期化
count = [0] * N
turn = 0

for _ in range(L):
    count[turn] += 1
    if count[turn] % 2 == 1:
        turn = a[turn] # 奇数回目は a の人が掃除
    else:
        turn = b[turn]  # 偶数回目は b の人が掃除

# 結果の出力
for i in range(N):
    print(a[i], b[i])
