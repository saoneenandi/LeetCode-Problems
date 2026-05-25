class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for i in range(len(nums)):
            numo = target - nums[i]
            if numo in seen:
                return [seen[numo], i]
            seen[nums[i]] = i
