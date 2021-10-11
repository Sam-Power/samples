nums1 = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
nums2 = [2,0,1]
# Output: [0,1,2]
nums3 = [0]
# Output: [0]
nums4 = [1]
# Output: [1]


a = [0 for i in range(nums1.count(0))]
b = [1 for i in range(nums1.count(1))]
c = [2 for i in range(nums1.count(2))]
a.extend(b)
a.extend(c)

