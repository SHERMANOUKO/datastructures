class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

#reverse a string using a stack
def reverse_string(stack, input_string):
    reversed_str = ""
    for i in range(len(input_string)):
        stack.push(input_string[i])

    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

# uncomment to test
# s = Stack()
# print(s.is_empty())
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# print(s.get_stack())
# print(s.peek())
# s.pop()
# print(s.get_stack())
# print(s.peek())
# print(s.is_empty())

# stack = Stack()
# print("Reversing string 'Sherman'")
# print(reverse_string(stack, 'Sherman'))
