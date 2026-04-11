from collections import deque

if __name__ == "__main__":
    line = list(input())
    stack = []
    for i in range(len(line)):
        if stack is not None:
            if line[i] == stack[-1]:
                stack.append(line[i])
            else:

        else:
            stack.append(line[i])

