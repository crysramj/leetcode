
"""
Link: https://leetcode.com/problems/two-sum/description/

Problem:
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.

"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        list_of_indexes = []
        
        for i in range(0, len(nums)):
            #start at the top index            
            test_num = nums[i]
            
            #get the remainder 
            remainder = target - test_num
            
            #check if that remainder exists in the list 
            if remainder in nums[i+1:]:
                
                remainder_indexes = []
            
                remainder_indexes += [index for index,element in enumerate(nums) \
                                     if element == remainder and index != i]
                
                #append indexes of values that sum to target
                list_of_indexes += [i,remainder_indexes.pop()]
                
                break

        return (list_of_indexes)