"""
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Problem:

Given the head of a sorted linked list, delete all duplicates such that
each element appears only once. Return the linked list sorted as well.


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head

        while curr and curr.next: #true 
            print(curr.val)
            if curr.val == curr.next.val:
                #unlink curr
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
    
#Test case

# solution = Solution()
#head = [1,1,2]
#solution.deleteDuplicates(head)