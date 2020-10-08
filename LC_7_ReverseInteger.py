"""
7. Reverse Integer
Easy

3792

5943

Add to List

Share
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0


Constraints:

-231 <= x <= 231 - 1

"""
class Solution:
    def reverse( self,x: int) -> int:
        a = [i for i in str(x)[::-1]]
        if "-" in a:
            a.insert(0, a.pop(len(a)-1))
        if pow(-2, 31) <= int("".join( a )) <= pow(2, 31) - 1:
            return int("".join( a ))
        else:
            return 0


u = 1534236469
print(Solution().reverse(u))
