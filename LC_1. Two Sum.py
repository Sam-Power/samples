"""
1. Two Sum
Easy

17261

618

Add to List

Share
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.



"""


class Solution:
    def twoSum( nums, target):
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                if target - nums[i] == nums[i]:
                    x = nums[i]
                    nums.remove(nums[i])
                    a = nums.index(target - x) +1
                    return [i,a]
                    break
                else:
                    a = nums.index(target - nums[i])
                    return [i,a]
                    break

nums = [3,2,4]
target = 6
print(Solution.twoSum(nums,target))


# solution2 Date 6 November 2020 Beats %75 with 36ms runtime
i= 0
j = len(nums)-1
temp = sorted(nums)
while i<j:
    if temp[i] + temp[j] == target:
        if temp[i] == temp[j]:
            x = nums.index(temp[i])
            nums.remove(temp[i])
            return x,nums.index(temp[j])+1
        else:
            return nums.index(temp[i]),nums.index(temp[j])
        break
    elif temp[i]+temp[j] > target:
        j-=1
    elif temp[i]+temp[j] < target:
        i+=1