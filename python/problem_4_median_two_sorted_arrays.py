
"""
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/

Problem:
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        median_nums = sorted(nums1 + nums2)
        index = len(median_nums)//2
        median = median_nums[index] if len(median_nums) % 2 == 1 else (median_nums[index]+median_nums[index-1])/2

        return (median)