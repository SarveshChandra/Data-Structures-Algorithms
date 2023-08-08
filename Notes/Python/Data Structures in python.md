# Data Structures in Python

Python has built-in support for some fundamental data structures. Here is a guide on how to implement and use them:

## 1. Arrays
Python doesn't have built-in support for arrays, but Python Lists can be used as arrays.

```python
array = [1, 2, 3, 4, 5]
```

## 2. Lists
Lists are mutable, ordered collections of items, and each item can be of a different type. They are similar to arrays.

```python
list = [1, "abc", 1.23, True]
```

## 3. Tuples
Tuples are similar to lists but are immutable. Once a tuple is created, you cannot change its values.

```python
tuple = (1, "abc", 1.23, True)
```

## 4. Map
In Python, the built-in dictionary data type serves as a hash map. So, you can use a dictionary to create a map data structure.

**Dictionaries**: Dictionaries are used to store key-value pairs.

```python
dictionary = {"name": "John", "age": 25, "city": "New York"}
```

```python
map = {}

# Insert key-value pairs into the map
map['key1'] = 'value1'
map['key2'] = 'value2'
map['key3'] = 'value3'

# Access values by their key
print(map['key1'])  # Output: 'value1'

# Delete a key-value pair from the map
del map['key1']

# Check if a key is in the map
if 'key1' in map:
    print('Key1 is in the map.')
else:
    print('Key1 is not in the map.')  # This line will be printed
```

## 5. Sets
Sets are used to store multiple items in a single variable. They are mutable, but they are unordered, unindexed, and every element is unique (no duplicates).

```python
set = {1, 2, 3, 4, 5}
```

## 6. Strings
Strings in Python are arrays of bytes representing Unicode characters.

```python
string = "Hello, World!"
```

## 7. Stacks
Python does not have a built-in stack data type, but a list can be used as a stack.

```python
stack = []
stack.append('a')  # push 'a' onto the stack
stack.append('b')  # push 'b' onto the stack
print(stack.pop())  # pop an item from the stack
```

```python
class Stack:
    def __init__(self):
        self.stack = []

    # Use list append method to push element in the stack
    def push(self, data):
        self.stack.append(data)

    # Use list pop method to remove element from the stack
    def pop(self):
        if len(self.stack) <= 0:
            return ("The Stack is empty")
        else:
            return self.stack.pop()

    # Display the stack
    def display(self):
        return self.stack
```

## 8. Queues
Python standard library has `queue` module which provides the functionalities of Queue data structure.

```python
from queue import Queue
q = Queue()
q.put('a')  # enqueue 'a'
q.put('b')  # enqueue 'b'
print(q.get())  # dequeue an item
```

```python
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    # Add an element
    def enqueue(self, item):
        self.queue.appendleft(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            print("No elements in Queue!")
            return None
        return self.queue.pop()

    # Display the queue
    def display(self):
        return self.queue
```

## 9. Linked Lists
You can define a class for linked list nodes and use these nodes to build a linked list.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node after a node
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Insert node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Deleting a node
    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Print the linked list
    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next
        print()
```

## 10. Matrix
Here is a simple implementation of a Matrix class in Python along with some common operations like addition, subtraction, multiplication, and transposition.

```python
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    # Matrix String Representation
    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += ' '.join(str(e) for e in row) + "\n"
        return matrix_str

    # Matrix Addition
    def add(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices are not the same size")
        
        result = []
        for row in range(self.rows):
            result.append(
                [self.matrix[row][col] + other.matrix[row][col] for col in range(self.columns)]
            )
        return Matrix(result)

    # Matrix Subtraction
    def subtract(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices are not the same size")
        
        result = []
        for row in range(self.rows):
            result.append(
                [self.matrix[row][col] - other.matrix[row][col] for col in range(self.columns)]
            )
        return Matrix(result)

    # Matrix Multiplication
    def multiply(self, other):
        if self.columns != other.rows:
            raise ValueError("Incompatible matrices for multiplication")
        
        result = []
        for row in range(self.rows):
            result_row = []
            for col in range(other.columns):
                product = sum(self.matrix[row][i] * other.matrix[i][col] for i in range(self.columns))
                result_row.append(product)
            result.append(result_row)
        return Matrix(result)

    # Matrix Transposition
    def transpose(self):
        result = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.columns)]
        return Matrix(result)
```

You can then create Matrix instances and call the defined methods like this:

```python
m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix 1:")
print(m1)

print("Matrix 2:")
print(m2)

print("Addition of Matrix 1 and Matrix 2:")
print(m1.add(m2))

print("Subtraction of Matrix 1 and Matrix 2:")
print(m1.subtract(m2))

print("Multiplication of Matrix 1 and Matrix 2:")
print(m1.multiply(m2))

print("Transposition of Matrix 1:")
print(m1.transpose())
```

## 11. Hash Table
A hash table, also known as a hash map, is a data structure that implements an associative array abstract data type, a structure that can map keys to values. Python's built-in `dict` type serves as a hash map. If you still want to implement your own hash table for learning purposes, below is a simple implementation of a hash table in Python. 

```python
class HashTable:
    def __init__(self):
        self.size = 100
        self.table = [None] * self.size

    def _hash_function(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def insert(self, key, value):
        key_hash = self._hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._hash_function(key)

        if self.table[key_hash] is None:
            return False

        for i in range (0, len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True
        return False
```

You can use this HashTable like this:

```python
h = HashTable()
h.insert('apple', 'delicious')
h.insert('banana', 'great')
h.insert('orange', 'citrus')
print(h.get('banana'))
h.delete('apple')
print(h.get('apple'))
```

This hash table uses a simple hash function, which just adds up the ASCII values of the characters in the key, and uses the modulus operator to keep the resulting hash within the range of the table size. This could cause collisions if different keys have the same sum of ASCII values. The hash table handles these collisions using separate chaining, where each slot in the hash table's array is a list of key-value pairs.

Please note that this is a very simple implementation, and real hash table implementations would use more sophisticated hash functions and techniques to handle collisions to ensure consistent performance even with a large number of entries.

## 12. Heap
In Python, you can easily use a built-in module called `heapq` to create and manipulate heaps. This module uses the list data structure to create a min heap by default.

However, if you want to implement your own heap for learning purposes, here is a simple implementation of a min heap:

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert_key(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_min(self):
        if not self.heap:
            return float('inf')
        root = self.heap[0]
        last_node = self.heap.pop()
        if self.heap:
            self.heap[0] = last_node
            self.heapify(0)
        return root

    def delete_key(self, i):
        self.decrease_key(i, float('-inf'))
        self.extract_min()

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < len(self.heap) and self.heap[i] > self.heap[l]:
            smallest = l
        if r < len(self.heap) and self.heap[smallest] > self.heap[r]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

```

You can use this `MinHeap` like this:

```python
h = MinHeap()
h.insert_key(3)
h.insert_key(2)
h.delete_key(1)
h.insert_key(15)
h.insert_key(5)
h.insert_key(4)
h.insert_key(45)
print(h.extract_min())
print(h.heap)
```

This implementation provides methods for inserting a key into the heap (`insert_key`), decreasing a key's value (`decrease_key`), extracting the minimum key (`extract_min`), deleting a key (`delete_key`), and for ensuring the heap property is maintained (`heapify`).

## 13. Tree (Binary Tree)
Here's a simple implementation of a binary tree in Python, with some commonly-used operations:

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    # Print the tree
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    # Depth-first traversals
    # Pre-order traversal
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.val) + " -> ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    # In-order traversal
    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.val) + " -> ")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    # Post-order traversal
    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.val) + " -> ")
        return traversal
    
    # Calculate the height of the tree
    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)
    
    # Level order (breadth-first) traversal
    def levelorder_print(self, start):
        if start is None:
            return 
        queue = [start]
        traversal = ""
        while len(queue) > 0:
            traversal += (str(queue[0].val) + " -> ")
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return traversal
    
    # Search for a value in the tree
    def search(self, find_val, start):
        if start:
            if start.val == find_val:
                return True
            else:
                return self.search(find_val, start.left) or self.search(find_val, start.right)
        return False
    
    # Insert a node
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.val:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

    # Find the minimum value
    def find_min(self):
        if self.root is None:
            return None
        else:
            return self._find_min(self.root)

    def _find_min(self, node):
        if node.left:
            return self._find_min(node.left)
        else:
            return node.val

    # Find the maximum value
    def find_max(self):
        if self.root is None:
            return None
        else:
            return self._find_max(self.root)

    def _find_max(self, node):
        if node.right:
            return self._find_max(node.right)
        else:
            return node.val
```

You can use the `BinaryTree` like this:

```python
# 1-2-4-5-3-6-7
#   Preorder
# 4-2-5-1-6-3-7
#   Inorder
# 4-5-2-6-7-3-1
#   Postorder
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print("Height of tree is %d" %(tree.height(tree.root)))
print("Level order traversal: " + tree.levelorder_print(tree.root))
print("Is 7 in the tree? " + str(tree.search(7, tree.root)))
print("Is 8 in the tree? " + str(tree.search(8, tree.root)))
```

This `BinaryTree` class supports three types of depth-first tree traversals: pre-order, in-order, and post-order. In a pre-order traversal, the root node is visited first, then the left subtree, and finally the right subtree. In an in-order traversal, the left subtree is visited first, then the root node, and finally the right subtree. In a post-order traversal, the left subtree is visited first, then the right subtree, and finally the root node.

Other methods and features could be added to this `BinaryTree` class depending on your specific needs, such as methods for breadth-first (level-order) traversal, inserting or deleting nodes, searching for a value, and so on.

Please note that the insert function assumes that the tree is a binary search tree, meaning all left descendants of a node are less than or equal to the node, and all right descendants are greater than the node.

The deletion of a node in a binary tree is a more complex operation and it's typically carried out in the following three steps:

    Find the node to be deleted: Start from the root and find the node containing the key to be deleted by making use of the binary search property.

    Delete the node: Once the node is found, delete it from the tree. There are three possible scenarios here:
        The node is a leaf node (has no children). In this case, just remove the node from the tree.
        The node has one child. In this case, replace the node with its subtree.
        The node has two children. This is the most complex case. Look for the in-order successor (the node which will come after the current node in in-order traversal) or the in-order predecessor (previous node in in-order traversal) and replace the node with the in-order successor or predecessor. After replacing, delete the in-order successor or predecessor. Typically the in-order successor (the minimum value in the right subtree) is used.

This is the most complex operation in a binary tree, and implementing it from scratch can be quite challenging and beyond the scope of this text, but there are many resources available online to guide you through this process if you're interested.