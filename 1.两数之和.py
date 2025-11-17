from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target-num], index]
            else:
                hash_map[num] = index

