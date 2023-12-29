# URL : https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j


myObj = Solution()
result = myObj.removeDuplicates([0,0,0,0,0,1,2,3,3,4])


