from typing import List

#灵神做法
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        length = len(nums)
        for i in range(length-2): # 这里比较重要，是枚举到倒数第三个
            x = nums[i]
            if i > 0 and x == nums[i-1]: # 这个判断也比较重要，可以去除掉重复的答案
                continue
            left, right = i+1, length-1
            while left < right:
                t = nums[left] + nums[right]
                if x + t < 0:
                    left += 1
                elif x + t > 0:
                    right -= 1
                else:
                    ans.append([x,nums[left],nums[right]])
                    # 下面的处理十分重要，确保了 j 和 k 也没有重复的情况。处理方式与处理i重复的情况一样 同时因为这里会对left 和 right做处理，所以需要最后判断是否 == -x的情况
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return ans


# 我的思路，尝试用set去重。可以成功，但是耗时较长
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        length = len(nums)
        for i in range(length-2): # 这里比较重要，是枚举到倒数第三个
            x = nums[i]
            left, right = i+1, length-1
            while left < right:
                if nums[left] + nums[right] < -x:
                    left += 1
                elif nums[left] + nums[right] > -x:
                    right -= 1
                else:
                    ans.add((x,nums[left],nums[right])) # 注意这里只能加入元组类型的数据，因为在集合中不可以加入列表这种不可变 不可哈希的元素
                    left += 1
                    right -= 1
        return [list(single_ans) for single_ans in ans]


#灵神第二种方法，加了个小优化
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        length = len(nums)
        for i in range(length-2): # 这里比较重要，是枚举到倒数第三个
            x = nums[i]
            if i > 0 and x == nums[i-1]: # 这个判断也比较重要，可以去除掉重复的答案
                continue
            left, right = i+1, length-1
            #优化就是下面这两处，好好琢磨一下为什么一个是break，一个是continue
            if x + nums[left] + nums[left+1] > 0:
                break
            if x + nums[right] + nums[right-1] < 0:
                continue
            while left < right:
                t = nums[left] + nums[right]
                if x + t < 0:
                    left += 1
                elif x + t > 0:
                    right -= 1
                else:
                    ans.append([x,nums[left],nums[right]])
                    # 下面的处理十分重要，确保了 j 和 k 也没有重复的情况。处理方式与处理i重复的情况一样 同时因为这里会对left 和 right做处理，所以需要最后判断是否 == -x的情况
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return ans
