from collections import deque

if __name__ == "__main__":
    line = list(input())
    stack1 = deque()     # '\'の位置
    stack2 = deque()     # (開始位置、面積)のペア
    area_sum = 0         #  水たまりの総面積
    area = 0             # 各水たまりの面積
    for i in range(len(line)):
        if line[i] == "\\":
            stack1.append(i)
        elif line[i] == "/":
            if stack1:
                j = stack1.pop()
                area = i - j
                area_sum += i - j
                while stack2 and stack2[-1][0] > j:
                    area += stack2.pop()[1]
                stack2.append((j, area))
    print(area_sum)
    areas = [area for _, area in stack2]
    print(len(stack2), *areas)
