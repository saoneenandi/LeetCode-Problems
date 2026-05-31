class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(int(digit) for digit in str(abs(n)))