"""
9. Palindrome Number
Easy

2708

1634

Add to List

Share
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?



Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false


Constraints:

-231 <= x <= 231 - 1

"""

#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        orig = x
        back_x = 0
        while x > 0:
            back_x = (back_x * 10) + (x % 10)
            x = x // 10
        return orig == back_x









