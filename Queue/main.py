# Queue implementation using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.head
        self.head = self.head.next
        del temp

    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.head.data

    def is_empty(self):
        return self.head is None


q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
while not q.is_empty():
    print(q.front())
    q.pop()  # 1 2 3 4
