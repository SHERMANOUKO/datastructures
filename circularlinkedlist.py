class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, data):
        new_node = Node(data)
        current_node = self.next
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break

    #linked list length
    def __len__(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
            if current_node == self.head:
                break
        return count

    #split circular linked list
    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        
        mid = size/2
        count = 0
        prev_node = None
        current_node = self.head

        while current_node and count < mid:
            count += 1
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = self.head

        split_cllist = CircularLinkedList()
        while current_node.next != self.head:
            split_cllist.append(current_node.data)
            current_node = current_node.next
        split_cllist.append(current_node.data)

        self.print_list()
        print('\n')
        split_cllist.print_list()

    #remove key
    def remove(self, key):
        if self.head.data == key:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = self.head.next
            self.head = self.head.next
        else:
            current_node = self.head
            prev_node = None

            while current_node.next != self.head:
                prev_node = current_node
                current_node = current_node.next
                if current_node.data == key:
                    prev_node.next = current_node.next
                    current_node = current_node.next

    #remove node
    def remove_node(self, node):
        if self.head == node:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = self.head.next
            self.head = self.head.next
        else:
            current_node = self.head
            prev_node = None

            while current_node.next != self.head:
                prev_node = current_node
                current_node = current_node.next
                if current_node == node:
                    prev_node.next = current_node.next
                    current_node = current_node.next

    #josephus problem
    def josephus_circle(self, step):
        current_node = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                current_node = current_node.next
                count += 1
            self.remove_node(current_node)
            current_node = current_node.next

    #check if linked list is circular
    def is_circular_linked_list(self, input_list):
        current_node = input_list.head
        while current_node.next:
            current_node = current_node.next
            if current_node.next = input_list.head:
                return True
        
        return False


clist = CircularLinkedList()
clist.append('C')
clist.append('D')
clist.append('E')
clist.append('F')
clist.append('B')
clist.append('A')
clist.print_list()
