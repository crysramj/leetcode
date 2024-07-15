"""
Link: https://leetcode.com/problems/remove-element/description/

Problem:
Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.
"""

class Solution:
    """This class removes an element from a list"""
    def remove_element(self, nums: list[int], val: int) -> int:
        """This method removes an element from a list"""
        j = 0

        #loop through all elements in nums
        for index,num in enumerate(nums):
            #check if value of the number in the array is equal to the val 
            if num == val:
                nums[index] = None
            elif num != val:
                #if no, then replace the first pointer with the number thats' not the val; j++
                nums[j] = num
                j+=1

        return j


#Test code
# a = Solution()
# a.remove_element([1,1,2,4,4,5,6,6,6,6],4)
