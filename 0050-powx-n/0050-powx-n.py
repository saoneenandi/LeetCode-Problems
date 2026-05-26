class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        current_product = x
        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2
        return result

        