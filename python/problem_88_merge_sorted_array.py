"""
Link: https://leetcode.com/problems/merge-sorted-array/description/

Problem:
You are given two integer arrays nums1 and nums2,
sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        x,y = m-1, n-1 #store end index for nums1 & nums2
        z = m + n - 1

        while y >= 0:
            #first compare x & y --> take max and move pointer z and x or y
            if x >= 0 and nums1[x] >= nums2[y]: 
                nums1[z] = nums1[x]
                x-=1
            else: 
                nums1[z] = nums2[y]
                y-=1
            z-=1  
            
        return (nums1)   

#Test case

# nums1 = [1,5,6,0,0,0]
# m = 3
# nums2 = [1,2,2]
# n = 3

# sol = Solution()
# sol.merge(nums1,m,nums2,3)