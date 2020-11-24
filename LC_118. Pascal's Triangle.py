"""118. Pascal's Triangle
Easy

1953

122

Add to List

Share
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        lst = [[1]]
        tmp = []
        for i in range(1,numRows):
            tmp.append(1)
            for j in range(len(lst[-1])-1):
                tmp.append( lst[-1][j] + lst[-1][j+1] )
            tmp.append(1)
            lst.append(tmp)
            tmp = []
        return lst

"""
Runtime: 28 ms, faster than 79.89% of Python3 online submissions for Pascal's Triangle.
"""