class Stack:
    """
    スタックデータ構造を実装するクラス
    
    Attributes:
        head (int): スタックの先頭位置を示すインデックス
        stack (list): スタックの要素を格納するリスト
    """
    def __init__(self):
        self.head: int = 0
        self.stack: list = []

    def append(self, value):
        self.stack.append(value)
        self.head += 1

    

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

