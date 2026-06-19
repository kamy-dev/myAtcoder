n = int(input())
A = [ int(_) for _ in input().split()]
q = int(input())
m = [ int(_) for _ in input().split()]

A_set = set()

# 再帰関数でAの和の組み合わせの集合 を作る
def A_sum_set(i: int, sum: int):
    if i == n:
        A_set.add(sum)
        return

    A_sum_set(i + 1, sum + A[i])
    A_sum_set(i + 1, sum)
    
A_sum_set(0,0)

for j in range(q):
    if m[j] in A_set:
        print("yes")
    else:
        print("no")

