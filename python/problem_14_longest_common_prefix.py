"""
Link: https://leetcode.com/problems/longest-common-prefix/description/

Problem:
Write a function to find the longest common
prefix string amongst an array of strings.

"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        first_word = strs[0]
        min_substring = first_word

        for word in strs[1:]:

            substring = ""
            #need to keep track of similar letters
            #compare word and str_1 
            min_len = min( len(word), len(first_word))
                        
            for i in range(0, min_len):
                if word[i] == first_word[i]:
                    substring += word[i]
                else:
                    break
            
            #override min_substring 
            if len(substring) < len(min_substring):
                min_substring = substring

        return (min_substring)
   

#Test case

# solution = Solution()
# strs = ["flower","flow","flight"]
# sol = Solution()
# sol.longestCommonPrefix(strs)