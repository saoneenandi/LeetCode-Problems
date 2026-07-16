class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        n = len(nums)
        prefixGcd = []
        current_max = nums[0]
        for num in nums:
            if num > current_max:
                current_max = num
            prefixGcd.append(get_gcd(num, current_max))
        prefixGcd.sort()
        total_sum = 0
        left = 0
        right = n - 1
        while left < right:
            total_sum += get_gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        return total_sum