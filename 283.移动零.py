from typing import List


#灵身的做法1，把nums当作栈
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack_size = 0
        for num in nums:
            if num != 0:
                nums[stack_size] = num
                stack_size += 1
        for index in range(stack_size, len(nums)):
            nums[index] = 0


#灵神的做法2，传统思路的交换做法，比较容易理解
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left_zero = 0
        for index, num in enumerate(nums):
            if num == 0:
                continue
            nums[index], nums[left_zero] = nums[left_zero], nums[index]
            left_zero += 1

