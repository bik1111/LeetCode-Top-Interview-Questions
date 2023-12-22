#url: https://leetcode.com/problems/two-sum/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found


a = Solution()
a.twoSum([3,2,4], 6)
