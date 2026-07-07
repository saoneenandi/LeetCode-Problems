class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        non_zero_digits = [char for char in str(n) if char != '0']
        if not non_zero_digits:
            return 0
        x = int("".join(non_zero_digits))
        digit_sum = sum(int(digit) for digit in non_zero_digits)
        return x * digit_sum        