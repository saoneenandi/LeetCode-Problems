class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank_map = {num: rank for rank, num in enumerate(sorted(set(arr)), 1)}
        return [rank_map[num] for num in arr]