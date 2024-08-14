"""
Link: 
https://leetcode.com/problems/find-common-characters/description/

Problem:
Given a string array words, return an array of all characters that show up in all strings within the words 
(including duplicates). You may return the answer in any order.

"""

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter

        first_word_cnt = Counter(words[0])

        for word in words:
            cur_cnt = Counter(word)

            for key in first_word_cnt:
                first_word_cnt[key] = min(first_word_cnt[key], cur_cnt[key]) #update the key with the min letter found between words

        #now first_word_cnt has key : min_key_ct in all words
        res = [key for key, val in first_word_cnt.items() for _ in range(val) if val > 0]

        return res
#Test case

# solution = Solution()
# sol = Solution()
# words = ["bella","label","roller"]
# sol.commonChars(words)
