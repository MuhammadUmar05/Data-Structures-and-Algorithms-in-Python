class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None


class DoublyList:
    def __init__(self):
        self.head = self.tail = None

    def push_front(self, data):
        new_node = Node(data)
        if not self.head:  # 1
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def pop_front(self):
        if not self.head:
            return
        temp = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        temp.next = None
        del temp

    def pop_back(self):
        if not self.head:
            return
        temp = self.tail  # 1 <=> 2 <=> 3 <=> NULL
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        temp.prev = None
        del temp

    def search(self, key):
        if not self.head:
            return
        temp = self.head
        index = 0
        while temp:
            if temp.data == key:
                return index
            temp = temp.next
            index += 1
        return -1

    def insert(self, data, position):
        size = self.length()
        if position < 0 or position > size:
            print("Invalid position")
            return
        if position == 0:
            self.push_front(data)
            return
        if position == size:
            self.push_back(data)
            return
        temp = self.head
        for i in range(position - 1):
            temp = temp.next  # 2 <=> 3 <=> 4 <=> 9 <=> 5 <=> NULL
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp
        if new_node.next:
            new_node.next.prev = new_node

    def length(self):
        temp = self.head
        size = 0
        while temp:
            temp = temp.next
            size += 1
        return size

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.next
        print("NULL")


dl = DoublyList()
dl.push_front(2)
dl.push_back(3)
dl.push_back(4)
dl.push_back(9)
dl.insert(1, 1)
dl.insert(5, 5)
print("Length of doubly linked list is", dl.length())
dl.display()
