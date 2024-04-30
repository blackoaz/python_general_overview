# Define the ListNode class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to convert a list into a linked list
def create_linked_list(values):
    # Create a dummy head and current pointer
    dummy_head = ListNode(0)
    current = dummy_head
    # Iterate through the list and create linked list nodes
    for value in values:
        current.next = ListNode(value)
        current = current.next
    # Return the head of the linked list
    return dummy_head.next

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values

# Define the Solution class with the addTwoNumbers method
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Initialize a dummy head and a current node
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Iterate through both linked lists
        while l1 is not None or l2 is not None:
            # Get values from l1 and l2 or 0 if they are None
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate sum and carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            current_digit = total_sum % 10
            
            # Create a new node with the current digit and attach it to the result list
            current.next = ListNode(current_digit)
            current = current.next
            
            # Move to the next nodes in the input linked lists, if available
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        # If there is any remaining carry, add it as a new node
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the next node of the dummy head, which is the head of the result linked list
        return dummy_head.next

# Create linked lists from the input lists
l1_linked_list = create_linked_list([2,4,3])
l2_linked_list = create_linked_list([5,6,4])

# Instantiate the solution and add the two numbers
solution = Solution()
result_linked_list = solution.addTwoNumbers(l1_linked_list, l2_linked_list)

# Print the result linked list
print(print_linked_list(result_linked_list))  # Output: [7, 0, 8]

