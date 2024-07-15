"""
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Problem:
Given an integer array nums sorted in non-decreasing order, r
emove the duplicates in-place such that each unique element appears only once.
 The relative order of the elements should be kept the same. 
 Then return the number of unique elements in nums.
"""

class Solution:
    """Class to remove duplicates"""
    def remove_duplicates(self, nums: list[int]) -> int:
        """Removes duplicates"""
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

#Test code
# a = Solution()
# a.remove_duplicates([1,1,2,4,4,5,6,6,6,6])
