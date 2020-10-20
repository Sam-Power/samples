def maxSlidingWindow(self, nums, k):
    d = collections.deque()
    out = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            out += nums[d[0]],
    return out


def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    q = collections.deque()
    output = []
    for i in range(len(nums)):
        # if the queue's left element is out of bounds, pop it to maintain size
        if i-k >= 0 and nums[i-k] == q[0]:
                q.popleft()

        # ensure array is DECREASING by right-popping elements that are smaller
        while q and q[-1] < nums[i]:
            q.pop()

        # add the element itself
        q.append(nums[i])

        # append to output list if we have full window
        if i >= k-1:
            output.append(q[0])

    return output