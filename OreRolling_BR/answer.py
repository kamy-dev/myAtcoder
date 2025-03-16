N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

# Retrieve the starting position
pi = 0
pj = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'A':
            pi = i # 例えば 11
            pj = j # 例えば 4

