class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
            
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    #print tree
    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder(tree.root, "")
        elif traversal_type == 'inorder':
            return self.inorder(tree.root, "")
        elif traversal_type =='postorder':
            return self.postorder(tree.root, "")
        elif traversal_type =='levelorder':
            return self.levelorder(tree.root)
        elif traversal_type =='reverselevelorder':
            return self.reverse_levelorder(tree.root)
        else:
            print("invalid choice")
            return False

    #preorder traversal
    def preorder(self, start, traversal):
        """root->left->right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    #inorder traversal
    def inorder(self, start, traversal):
        """left->root->right"""
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal

    #post order traversal
    def postorder(self, start, traversal):
        """left->right->root"""
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    #level order traversal
    def levelorder(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    #reverse level order traversal
    def reverse_levelorder(self, start):
        if start is None:
            return
        
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        
        return traversal

    #size of tree
    def size(self):
        if self.root is None:
            return 0

        size = 1
        stack = Stack()
        stack.push(self.root)
    
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

    #size of tree recursivelly
    def size_recursively(self, node):
        if node is None:
            return 0

        return 1 + self.size_recursively(node.left) + self.size_recursively(node.right)

    #heigh of tree
    def height(self, node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Printing preorder")
print(tree.print_tree("preorder"))

print("Printing inorder")
print(tree.print_tree("inorder"))

print("Printing postorder")
print(tree.print_tree("postorder"))

print("Printing levelorder")
print(tree.print_tree("levelorder"))

print("Printing levelorder")
print(tree.print_tree("reverselevelorder"))

print("Tree size")
print(tree.size())
print(tree.size_recursively(tree.root))

print("Tree height")
print(tree.height(tree.root))
