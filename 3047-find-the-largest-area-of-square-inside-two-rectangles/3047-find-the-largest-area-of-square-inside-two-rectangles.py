class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                width = min(topRight[i][0], topRight[j][0]) - max(bottomLeft[i][0], bottomLeft[j][0])
                height = min(topRight[i][1], topRight[j][1]) - max(bottomLeft[i][1], bottomLeft[j][1])
                if width > 0 and height > 0:
                    side = min(width, height)
                    ans = max(ans, side * side)
        return ans