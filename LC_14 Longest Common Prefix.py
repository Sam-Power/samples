# #daily-python-challenge
# QUESTION: Interview Level = Easy
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
class Solution:
    def longestCommonPrefix(self, strs):
        temp = res = ""
        if strs == []:
	        return ""
        for i in range(len(min(strs,key=len))):
            x = strs[0][i]
            for j in strs:
                if j[i]!=x:
                    return res
                else:
                    temp = j[i]
            res += temp
        return res

strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
strs3 = [""]
strs4 = []
strs5 =["cir","car"]
print(Solution().longestCommonPrefix(strs5))