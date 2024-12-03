class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None
        else:
            value = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return value

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.size - 1

    def display(self):
        print(self.stack[:self.top + 1])

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0

    def enqueue(self, value):
        if self.rear == self.size:
            print("Queue Overflow")
        else:
            self.queue[self.rear] = value
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("Queue Underflow")
            return None
        else:
            value = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            return value

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.rear == self.size
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def display(self):
        print(self.queue[self.front:self.rear])

class CirQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.start = -1
        self.end = -1

    def isFull(self):
        return (self.end + 1) % self.size == self.start

    def isEmpty(self):
        return self.start == -1

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[self.start]

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full! Cannot enqueue.")
            return None
        elif self.isEmpty():
            self.start = self.end = 0
        else:
            self.end = (self.end + 1) % self.size
        self.queue[self.end] = value

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty! Cannot dequeue.")
            return None
        value = self.queue[self.start]
        if self.start == self.end:
            self.start = self.end = -1
        else:
            self.start = (self.start + 1) % self.size
        return value

    def display(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        i = self.start
        while True:
            print(self.queue[i], end=" <- " if i != self.end else "")
            if i == self.end:
                break
            i = (i + 1) % self.size
        print()

######### LINKED LIST #########

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")  

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:  
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True 
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:  
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

######### DOUBLY LINKED LIST #########
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially no head
        self.tail = None  # Initially no tail
        self.length = 0    # Length is 0 initially
        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" <-> ")
            temp = temp.next
        print("None")
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        if self.length == 1:  # Handle the case where there's only one element
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
        
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:  # Handle case where there's only one element
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:  # Get from the start of the list
            for _ in range(index):
                temp = temp.next
        else:  # Get from the end of the list
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self,index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:  # Corrected to allow insertion at index == length
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

#STACK AND QUEUE USING LINKED LIST

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  
        self.height = 0  
        
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value, "->", end=" ")
            temp = temp.next
        print("None")
            
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None  
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

# Queue class using a linked list
class Queue:
    def __init__(self):
        self.first = None  
        self.last = None   
        self.length = 0    
        
    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
            
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            return None  
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
    
##### BST #####


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert a new key
    def insert(self, key):
        def _insert(root, key):
            if root is None:
                return Node(key)
            if key < root.key:
                root.left = _insert(root.left, key)
            elif key > root.key:
                root.right = _insert(root.right, key)
            return root

        self.root = _insert(self.root, key)

    # Delete a key
    def delete(self, key):
        def _delete(root, key):
            if root is None:
                return root

            if key < root.key:
                root.left = _delete(root.left, key)
            elif key > root.key:
                root.right = _delete(root.right, key)
            else:
                # Node with only one child or no child
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

                # Node with two children: Get the inorder successor
                successor = self.get_min(root.right)
                root.key = successor.key
                root.right = _delete(root.right, successor.key)

            return root

        self.root = _delete(self.root, key)

    # Get minimum value node
    def get_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    # Search for a key
    def search(self, key):
        def _search(root, key):
            if root is None or root.key == key:
                return root
            if key < root.key:
                return _search(root.left, key)
            return _search(root.right, key)

        return _search(self.root, key) is not None

    # Inorder traversal (LNR)
    def inorder(self):
        def _inorder(root):
            if root:
                _inorder(root.left)
                print(root.key, end=" ")
                _inorder(root.right)

        _inorder(self.root)

    # Preorder traversal (NLR)
    def preorder(self):
        def _preorder(root):
            if root:
                print(root.key, end=" ")
                _preorder(root.left)
                _preorder(root.right)

        _preorder(self.root)

    # Postorder traversal (LRN)
    def postorder(self):
        def _postorder(root):
            if root:
                _postorder(root.left)
                _postorder(root.right)
                print(root.key, end=" ")

        _postorder(self.root)


# DFS & BFS

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()

        def _dfs(node):
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    _dfs(neighbor)

        _dfs(start)

    def bfs(self, start):
        visited = set()
        queue = [start]  

        while queue:
            node = queue.pop(0)  
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor) 
