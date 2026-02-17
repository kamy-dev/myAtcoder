# 初期実装 O(n^2)のため、下でリングバッファを実装する。
# def round_robin(q: int, proc_list: list) -> None:
#     elapsed = 0
#     queue = list(proc_list)
#
#     while queue:
#         proc = queue.pop(0)
#         if proc[1] > q:
#             elapsed += q
#             proc[1] -= q
#             queue.append(proc)
#         else:
#             elapsed += proc[1]
#             print(proc[0], elapsed)
#
# if __name__ == "__main__":
#     n, q = map(int, input().split())
#     proc_list = []
#     for _ in range(n):
#         line = input().split()
#         proc_list.append([line[0], int(line[1])])
#
#     round_robin(q, proc_list)





if __name__ == "__main__":
    n, q = map(int, input().split())
    proc_list: list = []
    for _ in range(n):
        line: list[str] = input().split()
        proc_list.append([line[0], int(line[1])])
    
    head, tail = 0, 0
    queue = []
