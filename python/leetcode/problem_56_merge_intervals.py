"""
Link: https://leetcode.com/problems/merge-intervals/description/

Problem:
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input.

"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        index = 0
        
        intervals.sort() #sort list to make overlapping lists adjacent
        
        while index < len(intervals) - 1:
        
            first_list = intervals[index]
            second_list = intervals[index+1]

            if second_list[0] <= first_list[1]:
                #find beginning and end of interval for merge
                first_num = min(first_list[0], second_list[0])
                second_num = max(first_list[1], second_list[1])
                
                #drop first two items in index before in-place replacement
                intervals.pop(index)
                intervals.pop(index)
                #replace index 
                intervals.insert(index,[first_num,second_num])
                
            else:
                index += 1
  
        return (intervals)
    
    
    
#Test case

# solution = Solution()
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# sol = Solution()
# sol.merge(intervals)