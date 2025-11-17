from typing import List

#灵神方法
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n
        suf_max = [0] * n

        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], height[i])

        suf_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])

        ans = 0
        for h, premax, sufmax in zip(height, pre_max, suf_max):
            ans += min(premax, sufmax) - h
        return ans


#灵神思路2
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        premax = 0
        sufmax = 0
        left, right = 0, n-1
        while left < right:
            premax = max(premax, height[left])
            sufmax = max(sufmax, height[right])
            if premax < sufmax:
                ans += premax - height[left]
                left += 1
            else:
                ans += sufmax - height[right]
                right -= 1
        return ans






