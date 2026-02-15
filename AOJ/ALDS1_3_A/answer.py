def evaluate_rpn(l: list[str]) -> int:
    op = ["+", "-", "*"]
    stack = []
    
    for i in l:
        if i not in op:
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            if i == "+":
                stack.append(a + b)
            elif i == "-":
                stack.append(a - b)
            else:
                stack.append(a * b)

    return stack[0]

if __name__ == "__main__":
    l = input().split()
    print(evaluate_rpn(l))

