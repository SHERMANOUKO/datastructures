class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    #add node to end of list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    #add node to begining of list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #insert after a given node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node not in list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    #delete node
    def delete_node(self, key):
        current_node = self.head

        #checks if node to be deleted is the head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        #if the node to be deleted is not the head
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    #delete node given its position
    def delete_node_at_pos(self, pos):
        current_node = self.head
        if pos == 0:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        count = 1
        while current_node and count != pos:
            prev_node = current_node
            current_node = current_node.next
            count += 1

        if current_node is None:
            print("Position greater than no of list items")
            return

        prev_node.next = current_node.next
        current_node = None

    #length of list iteratively
    def list_length_iterative(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    #length of list recursively
    def list_length_recursive(self, node):
        if node is None:
            return 0

        return 1 + self.list_length_recursive(node.next)

    #swap nodes
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        current_node_1 = self.head
        while current_node_1 and current_node_1.data != key_1:
            prev_1 = current_node_1
            current_node_1 = current_node_1.next

        prev_2 = None
        current_node_2 = self.head
        while current_node_2 and current_node_2.data != key_2:
            prev_2 = current_node_2
            current_node_2 = current_node_2.next

        if not current_node_1 or not current_node_2:
            return

        if prev_1:
            prev_1.next = current_node_2
        else:
            self.head = current_node_2

        if prev_2:
            prev_2.next = current_node_1
        else:
            self.head = current_node_1

        current_node_1.next, current_node_2.next = current_node_2.next, current_node_1.next

    #help monitor how nodes are moving during reversing
    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ": "+ node.data)

    #iterratively reverse linkedlist
    def reverse_iterative(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            # self.print_helper(prev_node, "PREV NODE")
            # self.print_helper(current_node, "CURRENT NODE")
            # self.print_helper(next_node, "NEXT NODE")
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

    #iterate recursively
    def reverse_recursive(self):
        def _reverse_recursive(current_node,prev_node):
            if not current_node:
                return prev_node

            next_node = current_node.next
            current_node.next = prev_node
            # self.print_helper(prev_node, "PREV NODE")
            # self.print_helper(current_node, "CURRENT NODE")
            # self.print_helper(next_node, "NEXT NODE")
            prev_node = current_node
            current_node = next_node

            return _reverse_recursive(current_node,prev_node)
            
        self.head = _reverse_recursive(current_node=self.head,prev_node=None)

    #rotate list
    def rotate(self, k):
        p = self.head
        q = self.head
        prev_node = None
        count = 0

        while p and count < k:
            prev_node = p
            p = p.next
            q = q.next
            count += 1
        p = prev_node

        while q:
            prev_node = q
            q = q.next
        q = prev_node

        q.next = self.head
        self.head = p.next
        p.next = None

    #remove duplicates
    def remove_duplicates(self):
        current_node = self.head
        prev_node = None

        dup_values = dict()
        while current_node:
            if current_node.data in dup_values:
                #remove node
                prev_node.next = current_node.next
                current_node = None
            else:
                dup_values[current_node.data] = 1
                prev_node = current_node
            current_node = prev_node.next

    #print nth from last
    def print_nth_from_last(self, n):
        #uncomment method 1 to test method 1
        #method 1
        # total_len = self.list_length_iterative()
        # current_node = self.head
        # while current_node:
        #     if total_len == n:
        #         return current_node.data
        #     total_len -= 1
        #     current_node = current_node.next

        # if current_node is None:
        #     return

        #method 2
        p = self.head
        q = self.head

        count = 0
        while q and count < n:
            q = q.next
            count += 1

        while p and q:
            p = p.next
            q = q.next

        return p.data
        
    #count how many times a given data are in a list
    def count_occurrences_iterative(self, data):
        count = 0
        current_node = self.head
        while current_node:
            if current_node.data == data:
                count += 1
            current_node = current_node.next
        return count

    def count_occurrences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurrences_recursive(node.next, data)
        else:
            return self.count_occurrences_recursive(node.next, data)

    #merge 2 sorted linked lists
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q

        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        return new_head

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        sum_list = LinkedList()
        carry = 0

        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
           
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)

            if p:
                p = p.next
            if q:
                q = q.next
        sum_list.print_list()

    #move tail to head
    def move_tail_to_head(self):
        last_node = self.head
        second_last_node = None
        while last_node.next:
            second_last_node = last_node
            last_node = last_node.next

        last_node.next = self.head
        second_last_node.next = None
        self.head = last_node

llist = LinkedList()
llist.append('A')
llist.append('B') 
llist.append('C')
llist.append('D')
# llist.print_list()
llist.prepend('E')
# llist.print_list()
llist.insert_after_node(llist.head.next.next,'F')
# llist.print_list()
# print()
# llist.delete_node('E')
# llist.print_list()
# print()
# llist.delete_node_at_pos(3)
# llist.print_list()
# print()
# llist.swap_nodes('C','D')
# llist.print_list()
# print()
# llist.reverse_iterative()
# llist.reverse_recursive()
# llist.print_list()
# print()
# llist.rotate(3)
# llist.print_list()
llist.append('D')
llist.append('X')
llist.append('X')
llist.append('D')
# llist.print_list()
# print()
# llist.remove_duplicates()
# llist.print_list()
# print()
# print(llist.print_nth_from_last(3))
# print(llist.count_occurrences_iterative('D'))
# print(llist.count_occurrences_iterative('X'))
# print(llist.count_occurrences_recursive(llist.head, 'D'))
# print(llist.count_occurrences_recursive(llist.head, 'X'))

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

# llist_1.merge_sorted(llist_2)
# llist_1.print_list()
# llist_1.sum_two_lists(llist_2)
# llist.print_list()
# print()
# llist.move_tail_to_head()
# llist.print_list()
