""""A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:
Input: sentence = "leetcode"
Output: false"""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = "thequickbrownfoxjumpsoverthelazydog"
        alphabeth = sorted(list(set(a)))
        print(alphabeth)
        for i in set(sentence):
            if i in alphabeth:
                alphabeth.remove(i)
        if not alphabeth:
            return True
        else:
            return False
"""Runtime: 28 ms, faster than 95.26% of Python3 online submissions for Check if the Sentence Is Pangram.
Memory Usage: 14.3 MB, less than 20.01% of Python3 online submissions for Check if the Sentence Is Pangram."""