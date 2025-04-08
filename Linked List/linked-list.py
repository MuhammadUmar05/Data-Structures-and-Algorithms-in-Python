class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        # To add node at the beginning of the linked list
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def push_back(self, data):
        # To add node at the end of the linked list
        new_node = Node(data)
        if not self.head:  # 1 -> 2 -> 3
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def pop_front(self):
        # To remove node from the beginning of the linked list
        if not self.head:
            print("Linked List is empty")
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        del temp

    def pop_back(self):
        # To remove node from the end of the linked list
        if not self.head:
            print("Linked list is empty")
            return
        temp = self.head
        if self.head == self.tail:
            self.head = self.tail = None
            del temp
            return
        while temp.next != self.tail:  # 1-2-3-4
            temp = temp.next
        temp.next = None
        del self.tail
        self.tail = temp

    def search(self, key):
        # To find key in linked list
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

    def length(self):
        # To find the total number of nodes in linked list
        size = 0
        temp = self.head
        while temp:
            temp = temp.next
            size += 1
        return size

    def insert(self, data, position):
        # To insert node at any random position
        size = self.length()
        if position < 0 or position > size:
            print("Invalid Position")
            return
        if position == 0:
            self.push_front(data)
            return
        if position == size:
            self.push_back(data)
            return
        temp = self.head  # 1-2-4-5
        for i in range(position - 1):  # 2
            if not temp:
                print("Invalid Position")
                return
            temp = temp.next
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        # To print nodes of linked list
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


ll = List()
ll.push_back(21)
ll.push_back(4)
ll.push_back(9)
ll.push_front(16)
print("The length of linked list is", ll.length())
print(f"Key 9 is found at {ll.search(9)}")
ll.display()
