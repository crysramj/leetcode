"""
Link: https://leetcode.com/problems/merge-strings-alternately/description/

Problem:

You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.

"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word1_len, word2_len = len(word1), len(word2)
        min_char = min(word1_len, word2_len)
        ending = word2 if len(word2) > len(word1) else word1
        output_word = ""

        for i in range(min_char):
            output_word += (word1[i])
            output_word += (word2[i])

        output_word += ending[min_char:]

        return(output_word)   

#Test case

# solution = Solution()
# solution.mergeAlternately(word1 = "abc", word2 = "pqr")
