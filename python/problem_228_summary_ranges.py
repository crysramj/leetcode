"""
Link: https://leetcode.com/problems/summary-ranges/description/

Problem: 
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges,
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

"""

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        
        if len(nums) == 0:
            return

        start, end = 0, 0
        ranges_arr = []
        
        while end < len(nums)-1:
            
            #find end by iterate from start
            if int(nums[end+1]) - int(nums[end]) == 1: #if there's a one increment, increase end
                end += 1
            else:
                if start == end:
                    ranges_arr.append(f"{nums[start]}")
                else:
                    ranges_arr.append(f"{nums[start]}->{nums[end]}")
                #and update start
                start = end+1
                end = start
        
        #process final element
        if start == end:
            ranges_arr.append(f"{nums[start]}")
        else:
            ranges_arr.append(f"{nums[start]}->{nums[end]}")
            
        return (ranges_arr)    
    
    
    
#Test case

# nums =[0,2,3,4,6,8,9]
# sol = Solution()
# sol.summaryRanges(nums)