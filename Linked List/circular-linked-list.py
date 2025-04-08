class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = self.tail = None

    def push_front(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            self.tail.next = self.head
            return
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            self.tail.next = self.head
            return
        self.tail.next = new_node
        self.tail = new_node
        new_node.next = self.head

    def pop_front(self):
        if not self.head:  # 0 -> 1 -> 2 -> 3 -> 0
            return
        if self.head == self.tail:
            del self.head
            self.head = self.tail = None
            return
        temp = self.head
        self.head = self.head.next
        self.tail.next = self.head
        temp.next = None
        del temp

    def pop_back(self):
        if not self.head:
            return
        if self.head == self.tail:
            del self.head
            self.head = self.tail = None
            return
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next  # 0 -> 1 -> 2 -> 3 -> 0
        temp.next = self.head
        del self.tail
        self.tail = temp

    def display(self):
        print(self.head.data, end=" -> ")
        temp = self.head.next
        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp.data)


cl = CircularList()
cl.push_back(1)
cl.push_back(2)
cl.push_back(3)
cl.push_front(0)
cl.pop_front()
cl.pop_back()
cl.display()
