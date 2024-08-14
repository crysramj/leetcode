"""
Link: https://leetcode.com/problems/add-two-numbers/description/

Problem:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a 
single digit. Add the two numbers and return the sum as a linked list.

"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_list = []
        l2_list = []

        current = l1

        while current:
            l1_list.append(current.val)
            current = current.next

        current = l2

        while current:
            l2_list.append(current.val)
            current = current.next
    
        l1_val = ''
        l2_val = ''

        while l1_list:
            l1_val += str(l1_list.pop())

        while l2_list:
            l2_val += str(l2_list.pop())

        final_val = str(int(l1_val) + int(l2_val))

        # Initialize the head of the linked list
        final_list_node = ListNode(int(final_val[-1]))
        current = final_list_node

        # Iterate through the rest of the array and build the linked list
        for i in range(len(final_val)-2, -1, -1):
            new_node = ListNode(int(final_val[i]))
            current.next = new_node
            current = new_node  # Move to the newly created node

        return final_list_node
   

#Test case

# solution = Solution()
# l1 = [2,4,3]
# l2 = [5,6,4]
# solution.addTwoNumbers(l1,l2)
# Expected Output: [7,0,8]