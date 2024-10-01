"""
Link: https://leetcode.com/problems/roman-to-integer/description/ 

Problem:

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        
        total_sum = 0 
        i = 0

        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        #XL --> 40 --> 50 - 10

        while i < len(s) - 1:
            
            #compare current letter to next letter
            current_letter = s[i]
            next_letter = s[i+1]

            #if current letter is greater than next letter, just add num
            if roman_map[current_letter] >= roman_map[next_letter]:
                print('here')
                total_sum += roman_map[current_letter] 
                i += 1
            elif roman_map[current_letter] < roman_map[next_letter]:
                print('there')
                diff_ = roman_map[next_letter] - roman_map[current_letter]
                total_sum += diff_
                i += 2
            
            print (f"i: {i}; total_sum: {total_sum}")

        if i < len(s):
            total_sum += roman_map[s[i]]

        return total_sum


#Test case

# solution = Solution()
# solution.romanToInt("MCMXCIV")
