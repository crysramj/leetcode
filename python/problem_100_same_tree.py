"""
Link: https://leetcode.com/problems/same-tree

Problem:
Given the roots of two binary trees p and q, 
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #first base case: if they're both null
        if not p and not q: 
            return True
        #second base case: if one is null and the other is not
        if p and not q or not p and q:
            return False

        #third case --> check values on left and right
        if p.val == q.val:
            #check left and right nodes
            left_bool = self.isSameTree(p.left, q.left)
            right_bool = self.isSameTree(p.right, q.right)
            return (left_bool and right_bool)

#Test case
# p = [1,2] 
# q = [1,2,1]
# solution = Solution()
# solution.isSameTree(p,q)