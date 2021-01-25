class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a = b = ""
        for i in range(len(S)):
            if S[i] == '#':
                a = a[:-1]
            else:
                a += S[i]
        for i in range(len(T)):
            if T[i] == '#':
                b = b[:-1]
            else:
                b += T[i]

        if a == b:
            return True
        else:
            return False