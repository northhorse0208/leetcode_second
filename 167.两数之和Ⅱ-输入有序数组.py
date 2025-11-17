from typing import List

#灵神思路
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right: # 由于本题一定存在一个正确答案，所以这个可以直接 while True
            if numbers[left] + numbers[right] == target:
                break
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [left+1, right+1] # 题目中的序列下标是从1开始的