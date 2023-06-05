# Built-in data structures in python


## Lists:
Lists are one of the most common and versatile data structures in Python. They are used to store a collection of items, and can be modified by adding or removing items. Lists are denoted by square brackets [] and can contain any type of data, including other lists. Lists are used to store a collection of items, and can be modified by adding or removing items. Lists are denoted by square brackets [] and can contain any type of data, including other lists. Lists are useful for implementing dynamic arrays, stacks, queues, and other data structures.


## Tuples:
Tuples are similar to lists in that they can store a collection of items, but they are immutable, meaning they cannot be modified once they are created. Tuples are denoted by parentheses () and can contain any type of data. Tuples are similar to lists in that they can store a collection of items, but they are immutable, meaning they cannot be modified once they are created. Tuples are denoted by parentheses () and can contain any type of data. Tuples are useful for storing data that should not be changed, such as coordinates or constants. Tuples are a type of collection that stores a fixed-size collection of elements. They are immutable, which means that their contents cannot be changed once they are created. Tuples are useful for implementing algorithms that require fixed-size collections with immutable contents.


## Dictionaries:
Dictionaries are used to store a collection of key-value pairs. They are denoted by curly braces {} and the keys and values are separated by a colon (:). Dictionaries provide efficient methods for retrieving, adding, and deleting key-value pairs. Dictionaries are used to store a collection of key-value pairs. They are denoted by curly braces {} and the keys and values are separated by a colon (:). Dictionaries provide efficient methods for retrieving, adding, and deleting key-value pairs. Dictionaries are useful for implementing algorithms that require mapping one set of values to another.


## Strings:
Strings are used to represent text data in Python. They are denoted by either single quotes ('') or double quotes (""). Strings are immutable, meaning they cannot be modified once they are created, but you can perform various string operations such as concatenation, slicing, and formatting. Strings are used to represent text data in Python. They are denoted by either single quotes ('') or double quotes (""). Strings are immutable, meaning they cannot be modified once they are created, but you can perform various string operations such as concatenation, slicing, and formatting. Strings are useful for implementing algorithms that involve text manipulation, searching, and parsing.


## Byte arrays:
Byte arrays are used to represent a sequence of bytes. They are similar to strings, but they are mutable and can be modified by assigning new values to individual elements. Byte arrays are denoted by the built-in bytearray function. Byte arrays are used to represent a sequence of bytes. They are similar to strings, but they are mutable and can be modified by assigning new values to individual elements. Byte arrays are denoted by the built-in bytearray function. Byte arrays are useful for implementing algorithms that require efficient manipulation of binary data.


## Ranges:
Ranges are used to represent a sequence of numbers. They are commonly used for iterating over a sequence of numbers in a loop. Ranges are denoted by the built-in range function.


## Sets:
Sets are used to store a collection of unique items. They are denoted by curly braces {} and can contain any hashable data type. Sets provide efficient methods for checking if an item is in the set or for performing set operations such as union, intersection, and difference. Sets are useful for implementing algorithms that require checking for unique values or finding common elements in two or more collections. Sets are a type of collection that stores unique elements in no particular order. They provide efficient methods for set operations such as union, intersection, and difference. Sets are useful for implementing algorithms that require storing unique elements and performing set operations.


## Deque:
Deque is short for "double-ended queue". It is a data structure that allows adding and removing elements from both ends with O(1) time complexity. Python provides the collections module that includes a deque implementation. Deques are useful for implementing algorithms that require adding and removing elements from both ends, such as queueing and stack operations.


## Stacks:
Stacks are a type of data structure that follow the "Last In, First Out" (LIFO) principle. Elements are added to the top of the stack and removed from the top of the stack. Python's built-in list data structure can be used to implement a stack.


## Queues:
Queues are a type of data structure that follow the "First In, First Out" (FIFO) principle. Elements are added to the back of the queue and removed from the front of the queue. Python's built-in list data structure can be used to implement a queue, but it is less efficient than using the deque data structure from the collections module.


## Heaps:
Heaps are a type of binary tree that are used to efficiently maintain a collection of elements with a priority. The most common type of heap is the min-heap, which ensures that the smallest element is always at the top. Python's heapq module provides functions for creating and manipulating heaps.


## Trees:
Trees are a type of data structure that consists of nodes connected by edges. They are used to represent hierarchical relationships between data. Python's built-in dict data structure can be used to implement a tree.


## Graphs:
Graphs are a type of data structure that consists of nodes and edges that connect them. They are used to represent relationships between data that are not hierarchical. Python's dict data structure can be used to implement a graph.


## OrderedDict:
OrderedDict is a subclass of the dict data structure that maintains the order of the keys in which they were inserted. This data structure is useful for implementing algorithms that require maintaining the order of elements.


## Counter:
Counter is a subclass of the dict data structure that is used to count the occurrences of elements in a collection. It provides efficient methods for counting and retrieving the counts of elements. The Counter data structure is useful for implementing algorithms that require counting the occurrences of elements, such as frequency analysis.


## Namedtuple:
Namedtuple is a subclass of the tuple data structure that assigns names to the elements of the tuple. It provides an efficient way to create simple classes without defining a new class explicitly. Namedtuple is useful for implementing algorithms that require simple data structures with named fields.


## Enum:
Enum is a class that is used to represent a set of symbolic names. It provides a way to define a fixed set of values that can be used in place of magic numbers or strings. Enums are useful for implementing algorithms that require a fixed set of options, such as state machines.


## Defaultdict:
Defaultdict is a subclass of the dict data structure that provides a default value for non-existent keys. This data structure is useful for implementing algorithms that require a default value for missing keys, such as counting the occurrences of elements.


## Arrays:
Arrays are a type of data structure that stores a fixed-size homogeneous collection of elements. They provide efficient access to individual elements based on their indices. Arrays are useful for implementing algorithms that require fast access to elements in a fixed-size collection.


## BitArrays:
BitArrays are a type of array that stores bits instead of bytes. They provide an efficient way to store and manipulate bits, and are useful for implementing algorithms that require bit manipulation.