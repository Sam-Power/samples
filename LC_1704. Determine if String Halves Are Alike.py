"""You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.



Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
Example 3:

Input: s = "MerryChristmas"
Output: false
Example 4:

Input: s = "AbCdEfGh"
Output: true


Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters."""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        x = s[:len(s)//2]
        y = s[len(s)//2:]
        a = [i for i in x if i in vovels]
        b = [i for i in y if i in vovels]
        if len(a) != len(b):
            return False
        else :
            return True
"""Runtime: 36 ms, faster than 52.57% of Python3 online submissions for Determine if String Halves Are Alike.
Memory Usage: 14.5 MB, less than 8.09% of Python3 online submissions for Determine if String Halves Are Alike."""