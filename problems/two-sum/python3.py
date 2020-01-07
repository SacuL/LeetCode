# https://leetcode.com/problems/two-sum

#  Results:
# Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Two Sum.
# Memory Usage: 13.9 MB, less than 67.67% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for ix, num in enumerate(nums):
            if( (target - num) in dic ):
                return [dic[target - num], ix]
            dic[num] = ix
