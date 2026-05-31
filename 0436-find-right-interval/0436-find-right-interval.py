class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        sorted_starts = []
        for i, interval in enumerate(intervals):
            sorted_starts.append((interval[0], i))
        sorted_starts.sort()
        starts_only = [item[0] for item in sorted_starts]
        res = []
        for interval in intervals:
            end_val = interval[1]
            idx = bisect.bisect_left(starts_only, end_val)
            if idx < len(sorted_starts):
                res.append(sorted_starts[idx][1])
            else:
                res.append(-1)
        return res