"""
Link: 

Problem:
Given the root of a binary tree, invert the tree, and return its root.

"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return (root)

           

#Test case
#root = [4,2,7,1,3,6,9]
# solution = Solution()
#solution.invertTree(root)
