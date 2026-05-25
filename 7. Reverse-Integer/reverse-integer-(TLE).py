class Solution(object):
        def reverse(self, x):
            num=0
            while (x%10)!=0:
                digit = x%10
                num=digit+10*num
                x//10
            return num
