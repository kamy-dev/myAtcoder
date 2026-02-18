from typing import Any

# リングバッファを用いて、O(n)で実装する。
class Queue:
    def __init__(self, size: int) -> None:
        self.buffer: list[Any] = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0
        self.size = size

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.size

    def enqueue(self, value: Any) -> None:
        if self.is_full():
            raise Exception("Queue is full")
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.buffer[self.head]  
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return value

def round_robin(q: int, queue: Queue) -> None:
    elapsed = 0

    while not queue.is_empty():
        # このdequeueがO(1)となるように、Queueクラスを実装している。もしpop()の場合、O(n)となってしまう。
        proc = queue.dequeue()
        if proc[1] > q:
            elapsed += q
            proc[1] -= q
            queue.enqueue(proc)
        else:
            elapsed += proc[1]
            print(proc[0], elapsed)

if __name__ == "__main__":
    n, q = map(int, input().split())
    queue = Queue(n)
    for _ in range(n):
        line: list[str] = input().split()
        queue.enqueue([line[0], int(line[1])])
    
    round_robin(q, queue)

