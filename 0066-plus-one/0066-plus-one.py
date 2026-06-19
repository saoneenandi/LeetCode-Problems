class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int("".join(map(str, digits)))
        num=num+1
        result = [int(x) for x in str(num)]
        return(result)