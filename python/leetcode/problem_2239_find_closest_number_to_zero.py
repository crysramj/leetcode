"""
Link: https://leetcode.com/problems/find-closest-number-to-zero

Problem:

Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
If there are multiple answers, return the number with the largest value.

"""

class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        
        return_num = nums[0]

        for num in nums:
            print(f'num: {num}, return_num: {return_num}')
            if abs(num-0) <= abs(return_num):
                if abs(num) == return_num:
                    return_num = abs(num)    
                else:
                    return_num = num

        return return_num
#Test case

# solution = Solution()
# nums = [-4,-2,1,4,8]
# solution.findClosestNumber(nums)

