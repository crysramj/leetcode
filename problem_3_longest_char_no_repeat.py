
"""
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Problem:
Given a string s, find the length of the longest
substring
without repeating characters.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_strings = []
        
        #iterate through word index
        for index in range(0, len(s)):
            
            substring_ = ""
            
            word_to_start_with = s[index:] 
            
            #get the longest string starting from this index
            for index, letter in enumerate(word_to_start_with):
                if letter not in substring_:
                    substring_ += str(letter)
                else:
                    break
                    
            print(substring_)

            longest_strings.append(substring_)
        
        len_substrings = [len(word) for word in longest_strings]
        
        max_substring_length = max(len_substrings, default=0)

        return (max_substring_length)