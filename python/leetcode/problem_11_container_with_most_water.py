"""
Link: https://leetcode.com/problems/container-with-most-water/

Problem:
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            min_height = min(height[left],height[right]) #get the min
            width = (right-left)            
            area = min_height*width
            max_area = max(area, max_area)

            if height[left] > height[right]:
                right += -1 #update right
            else:
                left += 1

        return max_area

    
    
    
    
#Test case

# solution = Solution()
# height = [1,8,6,2,5,4,8,3,7]
# solution.maxArea(height)