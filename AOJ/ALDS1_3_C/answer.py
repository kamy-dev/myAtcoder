from __future__ import annotations

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None

    def __repr__(self):
        return f'Node({self.data!r})'

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def insert(self, data):
        """リストの先頭に新しいノードを挿入する"""
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def delete(self, data):
        """指定されたデータを持つ最初のノードを削除する"""
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def delete_first(self):
        """リストの先頭ノードを削除する"""
        if self.head is None:
            return
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

    def delete_last(self):
        """リストの末尾ノードを削除する"""
        if self.tail is None:
            return
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None

    def __str__(self):
        parts = []
        current = self.head
        while current is not None:
            parts.append(str(current.data))
            current = current.next
        return ' '.join(parts)

if __name__ == "__main__":
    n = int(input())

    linked_list = DoublyLinkedList()
    for _ in range(n):
        line = input().split()
        op = line[0]
        if op == "insert":
            linked_list.insert(int(line[1]))
        elif op == "delete":
            linked_list.delete(int(line[1]))
        elif op == "deleteFirst":
            linked_list.delete_first()
        elif op == "deleteLast":
            linked_list.delete_last()
    
    print(linked_list)
