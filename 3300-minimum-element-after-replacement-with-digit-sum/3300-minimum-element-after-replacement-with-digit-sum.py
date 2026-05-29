class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            digit_sum = 0
            n = nums[i]
            while n > 0:
                digit_sum += n % 10
                n //= 10
            nums[i] = digit_sum
        return min(nums)