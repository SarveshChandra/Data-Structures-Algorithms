'''Binary Search:
This function performs binary search on a sorted array to find the index of a given element. It has a time complexity of O(log n) and a space complexity of O(1).'''

def binary_search(arr, target):
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


'''Two-Pointers:
This function uses the two-pointers technique to find a pair of elements in an array that add up to a target value. It has a time complexity of O(n) and a space complexity of O(1).'''

def two_pointers(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
            
    return []


'''Sliding Window:
This function uses the sliding window technique to find the maximum sum of a subarray of a given size in an array. It has a time complexity of O(n) and a space complexity of O(1).'''

def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum


'''Frequency Counter:
This function uses a dictionary as a frequency counter to count the occurrences of each element in an array. It has a time complexity of O(n) and a space complexity of O(n).'''

def count_elements(arr):
    freq = {}
    for element in arr:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    return freq


'''Prefix Sum:
This function uses the prefix sum technique to compute the sum of elements in a subarray of an array in constant time. It has a time complexity of O(n) for pre-computation and O(1) for each query, and a space complexity of O(n).'''

def prefix_sum(arr):
    prefix_sum = [0]
    for i in range(len(arr)):
        prefix_sum.append(prefix_sum[-1] + arr[i])
    return prefix_sum

def subarray_sum(prefix_sum, left, right):
    return prefix_sum[right+1] - prefix_sum[left]


'''find_duplicate(nums: List[int]) -> int: This function takes a list of integers and returns the duplicate number in the list. It uses a hash set to keep track of the visited numbers and returns the first number that is already in the set.'''

def find_duplicate(nums: List[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


'''find_missing_number(nums: List[int]) -> int: This function takes a list of integers and returns the missing number in the list. It uses the Gauss' formula to calculate the sum of the first n natural numbers, subtracts the sum of the given list from the expected sum, and returns the difference.'''

def find_missing_number(nums: List[int]) -> int:
    expected_sum = (len(nums) * (len(nums) + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


'''rotate_array(nums: List[int], k: int) -> None: This function takes a list of integers and rotates it to the right by k positions in-place. It first reverses the entire list, then reverses the first k elements, and finally reverses the remaining elements.'''

def rotate_array(nums: List[int], k: int) -> None:
    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    k %= len(nums)
    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)


'''remove_duplicates(nums: List[int]) -> int: This function takes a sorted list of integers and removes any duplicate elements in-place. It uses two pointers to keep track of the last unique element found and the current element being examined. Whenever a unique element is found, it is moved to the next position in the list and the last unique element is updated.'''

def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    
    last_unique = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[last_unique]:
            last_unique += 1
            nums[last_unique] = nums[i]
            
    return last_unique + 1


'''merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]: This function takes two sorted lists of integers and returns a merged sorted list. It uses two pointers to traverse the two lists and adds the smaller element to the result list.'''

def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    i = j = 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            
    if i < len(arr1):
        merged.extend(arr1[i:])
    if j < len(arr2):
        merged.extend(arr2[j:])
        
    return merged


'''find_maximum_subarray_sum(nums: List[int]) -> int: This function takes a list of integers and returns the maximum subarray sum. It uses Kadane's algorithm to keep track of the maximum subarray sum seen so far and the current subarray sum.'''

def find_maximum_subarray_sum(nums: List[int]) -> int:
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
        
    return max_sum


'''find_pairs_with_given_sum(nums: List[int], target: int) -> List[Tuple[int, int]]: This function takes a list of integers and a target sum and returns all pairs of numbers that add up to the target. It uses a hash set to keep track of the complement of each number and the pairs found so far.'''

def find_pairs_with_given_sum(nums: List[int], target: int) -> List[Tuple[int, int]]:
    complements = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in complements:
            pairs.append((complement, num))
        complements.add(num)
        
    return pairs


'''find_missing_number(nums: List[int]) -> int: This function takes a list of integers that includes all numbers from 1 to n except one, and returns the missing number. It uses the formula for the sum of the first n natural numbers and subtracts the sum of the input list.'''

def find_missing_number(nums: List[int]) -> int:
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


'''rotate_array(nums: List[int], k: int) -> None: This function takes a list of integers and rotates it k times to the right. It uses slicing to create a new list with the rotated elements and then copies it back to the original list.'''

def rotate_array(nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n
    rotated = nums[n-k:] + nums[:n-k]
    nums[:] = rotated


'''find_duplicates(nums: List[int]) -> List[int]: This function takes a list of integers and returns a list of all duplicate elements. It uses a hash table to keep track of the frequency of each element.'''

def find_duplicates(nums: List[int]) -> List[int]:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return [num for num in freq if freq[num] > 1]


'''merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]: This function takes two sorted lists of integers and returns a new list that contains all elements from both lists, sorted in ascending order. It uses two pointers to traverse the input lists and merge them into a new list.'''

def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    i, j = 0, 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged += arr1[i:] + arr2[j:]
    return merged


'''find_max_sum_subarray(nums: List[int]) -> int: This function takes a list of integers and returns the maximum sum of any contiguous subarray. It uses Kadane's algorithm, which is based on the observation that the maximum sum of any subarray that ends at index i is either nums[i] or the sum of nums[i] and the maximum sum of any subarray that ends at index i-1.'''

def find_max_sum_subarray(nums: List[int]) -> int:
    max_sum = float('-inf')
    curr_sum = 0
    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum


'''find_kth_largest(nums: List[int], k: int) -> int: This function takes a list of integers and an integer k and returns the kth largest element in the list. It uses the built-in heapq module to maintain a heap of the k largest elements seen so far.'''

import heapq

def find_kth_largest(nums: List[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappushpop(heap, num)
    return heap[0]


'''two_sum(nums: List[int], target: int) -> List[int]: This function takes a list of integers and a target value, and returns the indices of the two elements in the list that add up to the target value. It uses a dictionary to store the complement of each element in the list and its index.'''

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


'''remove_duplicates(nums: List[int]) -> int: This function takes a sorted list of integers and removes any duplicates in place, returning the length of the modified list. It uses two pointers to track the current and next unique elements.'''

def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


'''rotate_array(nums: List[int], k: int) -> None: This function takes a list of integers and an integer k, and rotates the list to the right by k steps in place. It uses slicing to reverse the first len(nums)-k elements and the last k elements, then reverses the entire list.'''

def rotate_array(nums: List[int], k: int) -> None:
    k %= len(nums)
    nums[:len(nums)-k] = reversed(nums[:len(nums)-k])
    nums[len(nums)-k:] = reversed(nums[len(nums)-k:])
    nums.reverse()