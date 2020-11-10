"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = res = ""
        for i in s:
            if i not in temp:
                temp+=i
                if len(temp) > len(res):
                    res = temp
            else :
                temp = temp[temp.index(i)+1:] + i
        return len(res)



# Success
# Details
# Runtime: 48 ms, faster than 94.86% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
