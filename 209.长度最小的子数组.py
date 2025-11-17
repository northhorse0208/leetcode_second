from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        left, right = 0, 0
        sum = 0
        while right < len(nums):
            if sum < target:
                sum += nums[right]
                right += 1
            else:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
        if ans == float('inf'):
            return 0
        return ans