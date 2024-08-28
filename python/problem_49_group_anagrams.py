"""
Link: https://leetcode.com/problems/group-anagrams/

Problem:
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

"""

from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        result_dict = defaultdict(list)
        #for each term, find the counter and append the word to a result dictionary
        for word in strs:
            counter_word = dict(Counter(word))
            
            sorted_dict_word = {key: counter_word[key] for key in sorted(counter_word)}
            
            key = ''.join(f"{key}{value}" for key, value in sorted_dict_word.items())
            
            result_dict[key].append(word)
        
        res = [value for key, value in result_dict.items()]

        return (res)
    
#Test case
# strs = ["eat","tea","tan","ate","nat","bat"]
# sol = Solution()
# sol.groupAnagrams(strs)

