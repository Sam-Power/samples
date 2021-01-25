class Solution:
    def permute(self, nums):
        result = [[]]
        for sayi in nums:
            result = [ i + [j] for i in result for j in nums if j not in i  ]
            print(result)
    	#return result
print(Solution().permute([1,2,3]))