class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    #add a new node after another node
    def add_after_node(self, key, data):
        current_node = self.head
        while current_node:
            if current_node.next is None and current_node.data == key:
                self.append(data)
                return
            elif current.data == key:
                new_node = Node(data)
                nxt = current_node.next
                current_node.next = new_node
                new_node.next = nxt
                new_node.prev = current_node
                nxt.prev = new_node
            current_node = current_node.next

    #add a new node before another node
    def add_before_node(self, key, data):
        current_node = self.head
        while current_node:
            if current_node.prev is None and current_node.data == key:
                self.prepend(data)
                return
            elif current_node.data == key:
                new_node = Node(data)
                prev = current_node.prev
                prev.next = new_node
                current_node.prev = new_node
                new_node.next = current_node
                new_node.prev = prev
            current_node = current_node.next

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
