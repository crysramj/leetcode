"""
Link: https://leetcode.com/problems/binary-search/description/

Problem:
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity
"""

class Solution:
    """Class implementing Binary Search"""
    def search(self, nums: list[int], target: int) -> int:
        """Method to search for target in nums

        Args:
            nums (List[int]): array of numbers
            target (int): target value to search for in nums

        Returns:
            int: returns -1 if target can't be found or index if target is found
        """
        left_index, right_index = 0, len(nums) - 1

        while left_index <= right_index:

            mid_index = (left_index + right_index) // 2

            #if value of mid_index is less than the target, update the left index
            if nums[mid_index] < target:
                left_index = mid_index + 1
            #if value of mid_index is greater than the target, move the right inde
            elif nums[mid_index] > target:
                right_index  = mid_index - 1
            else:
                return mid_index

        return -1


#Test code
# a = Solution()
# a.search([-1,0,3,5,9,12], 9)
