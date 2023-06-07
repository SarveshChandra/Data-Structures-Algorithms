def gcd(a, b):

    '''gcd(a, b):
    This function computes the greatest common divisor of two integers a and b, using the Euclidean algorithm.'''

    if b == 0:
        return a
    return gcd(b, a % b)




def lcm(a, b):

    '''lcm(a, b):
    This function computes the least common multiple of two integers a and b, using the formula lcm(a, b) = (a * b) / gcd(a, b).'''

    return (a * b) // gcd(a, b)




def is_prime(n):

    '''is_prime(n): This function checks if an integer n is prime, using trial division up to the square root of n.'''

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True




def factorize(n):

    '''factorize(n): This function computes the prime factorization of an integer n, returning a list of prime factors and their multiplicities.'''

    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors




def binomial(n, k):

    '''binomial(n, k):
    This function computes the binomial coefficient n choose k, using dynamic programming.'''

    if k > n:
        return 0
    elif k == 0 or k == n:
        return 1
    else:
        c = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            c[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                c[i][j] = c[i-1][j-1] + c[i-1][j]
        return c[n][k]




class ListNode:

    '''reverse_linked_list(head):
    This function reverses a singly linked list, given its head node.'''
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev




def is_palindrome(s):

    '''is_palindrome(s): This function checks if a string s is a palindrome, ignoring whitespace and case.'''

    s = s.lower().replace(' ', '')
    return s == s[::-1]




def two_sum(nums, target):

    '''two_sum(nums, target): This function finds the indices of two numbers in a list nums that add up to a target value, using a dictionary to store the complement of each element.'''

    complement_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_map:
            return [complement_map[complement], i]
        complement_map[num] = i
    return []




def prime_sieve(n):

    '''prime_sieve(n): This function generates a list of all prime numbers up to a given integer n, using the Sieve of Eratosthenes algorithm.'''

    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i ** 2, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]




def permutations(nums):

    '''permutations(nums): This function generates all possible permutations of a list of integers nums, using backtracking.'''
    
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    result = []
    backtrack(0)
    return result




def matrix_rotation(matrix):

    '''matrix_rotation(matrix): This function rotates a 2D square matrix matrix 90 degrees clockwise, in-place.'''

    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
    return matrix




def merge_sort(arr):

    '''merge_sort(arr): This function sorts a list of integers arr using the merge sort algorithm.'''

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result




def binary_search(arr, target):

    '''binary_search(arr, target): This function searches for an integer target in a sorted list of integers arr using binary search.'''

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1




def count_chars(s):

    '''count_chars(s): This function counts the number of occurrences of each character in a string s, and returns a dictionary with the counts.'''

    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts




def generate_primes(n):

    '''generate_primes(n): This function generates all prime numbers up to a given integer n using the Sieve of Eratosthenes algorithm.'''

    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return primes




def factorial(n):

    '''factorial(n): This function calculates the factorial of a non-negative integer n.'''

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)




def fibonacci(n):

    '''fibonacci(n): This function calculates the n-th term of the Fibonacci sequence using dynamic programming.'''

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]




import heapq


def merge_sorted_lists(lists):

    '''merge_sorted_lists(lists): This function merges multiple sorted lists lists into a single sorted list using a heap. Returns the merged list.'''

    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heap.append((lst[0], i, 0))
    heapq.heapify(heap)
    merged = []
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        merged.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))
    return merged




def sort_dict_by_value(d):

    '''sort_dict_by_value(d): This function sorts a dictionary d by its values in ascending order. Returns the sorted dictionary as a list of tuples.'''

    return sorted(d.items(), key=lambda x: x[1])




def find_missing_number(arr):

    '''find_missing_number(arr): This function finds the missing number in a sequence of integers from 1 to n, where one of the numbers is missing. Returns the missing number.'''

    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)




def count_occurrences(arr, x):

    '''count_occurrences(arr, x): This function counts the number of occurrences of an element x in a list arr. Returns the count.'''

    return arr.count(x)




def merge_sort(arr):

    '''merge_sort(arr): This function performs a merge sort on a list arr, and returns a sorted copy of the original list.'''

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged




def count_sort(arr):

    '''count_sort(arr): This function performs a counting sort on a list arr of non-negative integers, and returns a sorted copy of the original list.'''

    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for val in arr:
        count[val] += 1
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    for val in arr:
        output[count[val] - 1] = val
        count[val] -= 1
    return output




def is_anagram(s1, s2):

    '''is_anagram(s1, s2): This function tests whether two strings s1 and s2 are anagrams of each other, i.e., contain the same characters in a different order.'''

    return sorted(s1) == sorted(s2)




def sum_digits(n):

    '''sum_digits(n): This function returns the sum of the digits of a non-negative integer n.'''

    return sum(int(d) for d in str(n))




def next_permutation(arr):

    '''next_permutation(arr): This function generates the lexicographically next permutation of a list arr, or returns None if no such permutation exists.'''

    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    if i < 0:
        return None
    j = len(arr) - 1
    while j > i and arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = reversed(arr[i+1:])
    return arr




def subset_sum(nums, target):

    '''subset_sum(nums, target): This function finds whether there exists a subset of a list nums that sums up to a given target.'''

    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    return dp[n][target]




def merge_intervals(intervals):

    '''merge_intervals(intervals): This function merges overlapping intervals in a list of intervals intervals.'''

    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    return merged




def permutations(arr, r):

    '''permutations(arr, r): This function returns all possible permutations of a list arr of length r.'''

    if r == 0:
        yield []
    else:
        for i in range(len(arr)):
            for perm in permutations(arr[:i] + arr[i+1:], r-1):
                yield [arr[i]] + perm




def combinations(arr, r):

    '''combinations(arr, r): This function returns all possible combinations of a list arr of length r.'''

    if r == 0:
        yield []
    elif r == len(arr):
        yield arr
    else:
        for i in range(len(arr) - r + 1):
            for comb in combinations(arr[i+1:], r-1):
                yield [arr[i]] + comb




import heapq

def dijkstra(graph, start):

    '''dijkstra(graph, start): This function computes the shortest path from a starting node start to all other nodes in a weighted directed graph graph using Dijkstra's algorithm.'''

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        (dist, node) = heapq.heappop(heap)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return distances




def topological_sort(graph):

    '''topological_sort(graph): This function performs a topological sort on a directed acyclic graph (DAG) represented as an adjacency list graph.'''

    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    queue = [node for node in in_degree if in_degree[node] == 0]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(result) != len(graph):
        raise ValueError("Graph contains a cycle.")
    return result




def bfs(graph, start):

    '''bfs(graph, start): This function performs a breadth-first search on a graph graph starting at node start.'''

    visited = {node: False for node in graph}
    queue = [start]
    visited[start] = True
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)




def get_divisors(n):

    '''get_divisors(n): This function returns a list of all divisors of an input integer n.'''

    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)




def gcd_extended(a, b):

    '''gcd_extended(a, b): This function calculates the extended greatest common divisor (GCD) of two numbers a and b, returning the GCD and two coefficients x and y such that ax + by = gcd(a, b).'''

    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcd_extended(b, a % b)
        return d, y, x - (a // b) * y




def manhattan_distance(p1, p2):

    '''manhattan_distance(p1, p2): This function calculates the Manhattan distance between two points p1 and p2, represented as tuples.'''
    
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])