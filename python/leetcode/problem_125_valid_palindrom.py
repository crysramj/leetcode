"""
Link: https://leetcode.com/problems/valid-palindrome/description/

Problem:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s)-1
        
        while left < right:
            if s[left].lower().isalpha() and s[right].lower().isalpha() and s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            elif not s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1
            else:
                return False
                
            return True
            
        return 
    
#Test case

# solution = Solution()
# s = "A man, a plan, a canal: Panama"
# solution.isPalindrome(s)


