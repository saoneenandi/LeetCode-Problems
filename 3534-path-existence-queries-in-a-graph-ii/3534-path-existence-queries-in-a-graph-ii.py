class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        A = sorted(list(set(nums)))
        m = len(A)
        
        # LOG = 18 is enough since 2^17 = 131,072 > 10^5
        LOG = 18
        
        # up[i][j] stores the index reached from unique index i after 2^j greedy steps
        up = [[0] * LOG for _ in range(m)]
        
        # 2. Initialize the base cases (2^0 = 1 step)
        for i in range(m):
            # Find the largest element in A that is <= A[i] + maxDiff
            ub = bisect_right(A, A[i] + maxDiff)
            up[i][0] = ub - 1
            
        # Build the binary lifting table
        for j in range(1, LOG):
            for i in range(m):
                up[i][j] = up[up[i][j - 1]][j - 1]
                
        # 3. Process the queries
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            X = min(nums[u], nums[v])
            Y = max(nums[u], nums[v])
            
            # Find starting index of value X in our unique array A
            curr = bisect_left(A, X)
            steps = 0
            
            # Lift greedily as long as the value reached is strictly less than Y
            for j in range(LOG - 1, -1, -1):
                if A[up[curr][j]] < Y:
                    steps += (1 << j)
                    curr = up[curr][j]
            
            # Take one final hop to see if Y can be covered or spanned
            final_idx = up[curr][0]
            if A[final_idx] >= Y and Y - A[curr] <= maxDiff:
                ans.append(steps + 1)
            else:
                ans.append(-1)
                
        return ans