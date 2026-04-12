from typing import List

# LinearSearchを実装
def linearSearch(n: int, t: List[int]) -> int:
    idx = 0
    while idx < len(t):
        if t[idx] != n:
            idx += 1
        else:
             return True
    return False

if __name__ == "__main__":
    n = int(input())
    s = list(map(int, input().split()))
    q = int(input())
    t = list(map(int, input().split()))
    ans = set() # 重複を避けるためにsetを使用 
    i = 0
    while i < n:    
        if linearSearch(s[i], t):
            ans.add(s[i])
        i += 1
    print(len(ans))

# 初回回答：Tの中にSの要素があるかどうかを確認
# for i in range(q):
#     for j in range(n):
#         if s[j] == t[i]:
#             if t[i] not in ans:
#                 ans.append(t[i])    
#
# print(len(ans))

# 別解
# n = input()
# s = set(input().split())
# q = input()
# t = set(input().split())
# print(len(s & t))

