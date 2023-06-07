'''Node class
We will start with defining a Node class which represents each node in the linked list.'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


'''Helper function to create a linked list
The following function takes a list of values and returns the head node of a linked list with those values.'''

def create_linked_list(vals):
    head = Node(0)
    curr = head
    for val in vals:
        curr.next = Node(val)
        curr = curr.next
    return head.next


'''Helper function to print a linked list
This function takes the head node of a linked list and prints all the values in the list.'''

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


'''Helper function to reverse a linked list
This function takes the head node of a linked list and returns the new head node of the reversed list.'''

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


'''Helper function to find the middle node of a linked list
This function takes the head node of a linked list and returns the middle node of the list. If the list has an even number of nodes, it returns the second middle node.'''

def find_middle_node(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


'''Helper function to find the nth node from the end of a linked list
This function takes the head node of a linked list and an integer n and returns the nth node from the end of the list.'''

def find_nth_node_from_end(head, n):
    fast = head
    for i in range(n):
        if fast:
            fast = fast.next
        else:
            return None
    slow = head
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


'''Helper function to merge two sorted linked lists
This function takes the head nodes of two sorted linked lists and returns the head node of a merged sorted linked list.'''

def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    curr = dummy
    while head1 and head2:
        if head1.val < head2.val:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    curr.next = head1 or head2
    return dummy.next


'''Helper function to detect cycle in a linked list
This function takes the head node of a linked list and returns True if the list contains a cycle, False otherwise.'''

def detect_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


'''Helper function to find the starting node of a cycle in a linked list
This function takes the head node of a linked list with a cycle and returns the starting node of the cycle.'''

def find_cycle_start(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


'''Helper function to remove the nth node from the end of a linked list
This function takes the head node of a linked list and an integer n and removes the nth node from the end of the list.'''

def remove_nth_node_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = head
    for i in range(n):
        fast = fast.next
    slow = dummy
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next


'''Helper function to delete a node from a linked list
This function takes a node in a linked list (except the tail node) and removes it from the list.'''

def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next


'''Helper function to find the intersection of two linked lists
This function takes the head nodes of two linked lists that intersect at some point and returns the intersection node.'''

def find_intersection(head1, head2):
    len1, len2 = 0, 0
    curr1, curr2 = head1, head2
    while curr1:
        len1 += 1
        curr1 = curr1.next
    while curr2:
        len2 += 1
        curr2 = curr2.next
    curr1, curr2 = head1, head2
    if len1 > len2:
        for i in range(len1 - len2):
            curr1 = curr1.next
    else:
        for i in range(len2 - len1):
            curr2 = curr2.next
    while curr1 != curr2:
        curr1 = curr1.next
        curr2 = curr2.next
    return curr1


'''Helper function to reverse a linked list
This function takes the head node of a linked list and returns the head node of the reversed list.'''

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


'''Helper function to merge two sorted linked lists
This function takes the head nodes of two sorted linked lists and returns the head node of the merged list.'''

def merge_lists(head1, head2):
    dummy = Node(0)
    curr = dummy
    while head1 and head2:
        if head1.val < head2.val:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    curr.next = head1 or head2
    return dummy.next


'''Helper function to remove duplicates from a sorted linked list
This function takes the head node of a sorted linked list and removes any duplicates from the list.'''

def remove_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


'''Helper function to add two numbers represented by linked lists
This function takes the head nodes of two linked lists that represent non-negative integers and returns the head node of the resulting linked list that represents the sum of the two integers.'''

def add_lists(l1, l2):
    dummy = Node(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        carry, digit = divmod(val1 + val2 + carry, 10)
        curr.next = Node(digit)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next


'''Helper function to remove nodes with a certain value from a linked list
This function takes the head node of a linked list and a value and removes any nodes from the list that have that value.'''

def remove_value(head, value):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr:
        if curr.val == value:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next


'''Helper function to split a linked list into two halves
This function takes the head node of a linked list and returns the head nodes of the two halves of the list. If the list has an odd number of nodes, the first half will have one more node than the second half.'''

def split_list(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second_half = slow.next
    slow.next = None
    return head, second_half


'''Helper function to reorder a linked list
This function takes the head node of a linked list and reorders the list so that the first node is followed by the last node, the second node is followed by the second-to-last node, and so on.'''

def reorder_list(head):
    if not head or not head.next:
        return head
    # Split the list into two halves
    first_half, second_half = split_list(head)
    # Reverse the second half of the list
    second_half = reverse_list(second_half)
    # Merge the two halves
    curr = first_half
    while second_half:
        next1 = curr.next
        next2 = second_half.next
        curr.next = second_half
        second_half.next = next1
        curr = next1
        second_half = next2
    return first_half


'''Helper function to find the middle node of a linked list
This function takes the head node of a linked list and returns the middle node of the list. If the list has an even number of nodes, the second of the two middle nodes is returned.'''

def find_middle_node(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


'''Helper function to check if a linked list is a palindrome
This function takes the head node of a linked list and returns True if the list is a palindrome (i.e., reads the same forwards and backwards), and False otherwise.'''

def is_palindrome(head):
    # Find the middle node of the list
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Reverse the second half of the list
    second_half = reverse_list(slow)
    # Compare the first half and second half of the list
    curr1 = head
    curr2 = second_half
    while curr1 and curr2:
        if curr1.val != curr2.val:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    return True


'''Helper function to find the intersection point of two linked lists
This function takes the head nodes of two linked lists and returns the node at which the two lists intersect. If the two lists do not intersect, None is returned.'''

def get_intersection_node(head1, head2):
    curr1 = head1
    curr2 = head2
    len1 = 0
    len2 = 0
    # Find the length of the first list
    while curr1:
        len1 += 1
        curr1 = curr1.next
    # Find the length of the second list
    while curr2:
        len2 += 1
        curr2 = curr2.next
    # Make the two lists the same length
    curr1 = head1
    curr2 = head2
    while len1 > len2:
        curr1 = curr1.next
        len1 -= 1
    while len2 > len1:
        curr2 = curr2.next
        len2 -= 1
    # Traverse the two lists until they intersect
    while curr1 and curr2:
        if curr1 == curr2:
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next
    return None


'''Helper function to remove the Nth node from the end of a linked list
This function takes the head node of a linked list and an integer N, and removes the Nth node from the end of the list.'''

def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    slow = dummy
    fast = head
    # Move the fast pointer N nodes ahead of the slow pointer
    for i in range(n):
        fast = fast.next
    # Move the slow and fast pointers until the end of the list
    while fast:
        slow = slow.next
        fast = fast.next
    # Remove the Nth node
    slow.next = slow.next.next
    return dummy.next


'''Helper function to reverse a linked list between two given nodes
This function takes the head node of a linked list and two nodes, prev_node and end_node, and reverses the sublist between them (inclusive of prev_node and end_node). This function returns the head node of the reversed list.'''

def reverse_between(head, prev_node, end_node):
    # Set the current and previous nodes
    curr = prev_node.next
    prev = prev_node
    # Reverse the sublist between prev_node and end_node
    while curr != end_node:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    # Connect the reversed sublist with the rest of the list
    prev_node.next.next = curr
    prev_node.next = prev
    return head


'''Helper function to merge two sorted linked lists
This function takes the head nodes of two sorted linked lists and merges them into a single sorted linked list. This function returns the head node of the merged list.'''

def merge_lists(head1, head2):
    dummy = Node(0)
    curr = dummy
    curr1 = head1
    curr2 = head2
    # Traverse both lists and merge them
    while curr1 and curr2:
        if curr1.val < curr2.val:
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next
        curr = curr.next
    # Append the remaining nodes from the non-empty list
    if curr1:
        curr.next = curr1
    else:
        curr.next = curr2
    return dummy.next


'''Helper function to sort a linked list using merge sort
This function takes the head node of a linked list and returns the head node of the sorted list using the merge sort algorithm.'''

def merge_sort(head):
    # Base case: empty or one node list
    if not head or not head.next:
        return head
    # Find the middle node of the list
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Split the list into two halves
    second_half = slow.next
    slow.next = None
    # Recursively sort each half of the list
    head1 = merge_sort(head)
    head2 = merge_sort(second_half)
    # Merge the two sorted halves of the list
    return merge_lists(head1, head2)