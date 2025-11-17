from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        num_hash = set(nums)
        for num in num_hash: #这里遍历的一定是哈希后的集合，而不是哈希前的列表
            if num - 1 in num_hash: #这里注意，如果一个值他前面的值已经存在了，那么就没必要从他开始了
                continue
            length = 1
            while True:
                if num + length in num_hash:
                    length += 1
                else:
                    break
            if length > len(nums) / 2: # 最终优化，由于序列都是独立的，所以如果一个序列的长度已经是一半以上了，那么他肯定时最长子序列
                return length
            ans = max(ans, length)
        return ans