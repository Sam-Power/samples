"""Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.



Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3."""


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = 3
        res = sum(arr)
        while n <= len(arr):
            for i in range(len(arr)):
                if len(arr[i:n+i]) == n:
                    res += sum( arr[i:n+i] )

            n+=2
        return res

"""Runtime: 88 ms, faster than 24.54% of Python3 online submissions for Sum of All Odd Length Subarrays.
Memory Usage: 14.4 MB, less than 20.02% of Python3 online submissions for Sum of All Odd Length Subarrays."""