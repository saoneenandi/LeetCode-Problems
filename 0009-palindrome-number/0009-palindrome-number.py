class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        original_num = x
        reversed_num = 0
        while x != 0:
            digit = x % 10
            reversed_num = (reversed_num * 10) + digit
            x //= 10

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return False
        
        if (reversed_num == original_num):
            return True
        else:
            return False
        