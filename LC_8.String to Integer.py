class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        for i in s:
            if i not in ["-","+",'1','2','3','4','5','6','7','8','9','0', " "] and not res:
                return 0
            if res and i in ["-","+"]:
                try:
                    return int(res) if int(res)<=((2**31)-1) and int(res) >= (-2**31) else (-2147483648 if int(res) < (-2**31) else 2147483647)
                except:
                    return 0
            if i not in ["-","+",'1','2','3','4','5','6','7','8','9','0'] and len(res):
                try:
                    return int(res) if int(res)<=((2**31)-1) and int(res) >= (-2**31) else (-2147483648 if int(res) < (-2**31) else 2147483647)
                except:
                    return 0
            if i in ["-","+",'1','2','3','4','5','6','7','8','9','0']:
                res += i
        if res == '+' or res =="-":
            return 0
        if not res:
            return 0
        return int(res) if int(res)<=((2**31)-1) and int(res) >= (-2**31) else (-2147483648 if int(res) < (-2**31) else 2147483647)
s1 = "4193 with words"
s2 = "words and 987"
s3 = "42"
s4 = "   -42"
s5 = "-91283472332"
s6 = ".1"
s7 = "+-12"
s8 = "-5-"

print( Solution().myAtoi(s8) )