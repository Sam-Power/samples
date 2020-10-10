"""
20. Valid Parentheses
Easy

5800

241

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


"""
class Solution:
    def isValid(self, s: str) -> bool:
        lst = ["()","[]","{}"]
        if len(s)%2 == 0:
            for i in range(int(len(s)/2)):
                for x in lst:
                    if x in s:
                        s = s.replace(x,"")
            if s == "":
                return True
            else:
                return False
        else:
            return False

print(Solution().isValid(s = "{[]}"))

