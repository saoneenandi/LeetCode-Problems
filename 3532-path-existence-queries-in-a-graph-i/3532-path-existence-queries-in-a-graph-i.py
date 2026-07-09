class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        components = [0] * n
        curr_id = 0
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr_id += 1
            components[i] = curr_id
        ans = []
        for u, v in queries:
            ans.append(components[u] == components[v])
            
        return ans