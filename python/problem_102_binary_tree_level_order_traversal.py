"""
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Problem:
Given the root of a binary tree,
return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: #if null
            return []
        
        queue = [] #add nodes here
        res = []

        queue.append(root) #append root

        while queue: #while queue is not empty          
            level = [] #add node values here

            for i in range(len(queue)):
                #process the value of the node
                node = queue.pop(0) #O(n) and deque is better with popleft in O(1) time
                level.append(node.val)

            res.append(level) #add the nodes from that level

            if node.left: queue.append(node.left) #add left and right nodes of children
            if node.right: queue.append(node.right) #add left and right nodes of children
            #repeat process for next value in queue

        return res 

#Test case
#root = [3,9,20,null,null,15,7]
# solution = Solution()
# solution.levelOrder(root)
