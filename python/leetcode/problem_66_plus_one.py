"""
Link: https://leetcode.com/problems/plus-one/description/

Problem:
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    """This class increments the large integer by one
    """
    def plus_one(self, digits: list[int]) -> list[int]:
        """This method adds one

        Args:
            digits (list[int]): list of digits

        Returns:
            list[int]: list of digits incremented  by one
        """
        num = ""
        res = []

        for digit in digits:
            num += str(digit)

        int_num_incremented = int(num)+1

        for digit in str(int_num_incremented):
            res.append(int(digit))

        return res


#Test code
# a = Solution()
# a.plus_one([4,4])
