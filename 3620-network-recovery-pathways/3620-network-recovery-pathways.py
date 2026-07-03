from collections import deque

class Solution:
    def findMaxPathScore(self, edges, online, k):
        # Calculate n dynamically from the length of the online list
        n = len(online)
        
        # Step 1: Build adjacency list and calculate in-degrees
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for u, v, cost in edges:
            adj[u].append((v, cost))
            in_degree[v] += 1
            
        # Step 2: Find the topological ordering
        topo_order = []
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v, _ in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # Step 3: Feasibility check function
        def can_reach_with_min_cost(min_allowed_edge):
            dp = [float('inf')] * n
            dp[0] = 0
            
            for u in topo_order:
                if dp[u] == float('inf'):
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                    
                for v, cost in adj[u]:
                    if cost >= min_allowed_edge:
                        if dp[u] + cost < dp[v]:
                            dp[v] = dp[u] + cost
                            
            return dp[n - 1] <= k

        # Step 4: Binary Search over the possible minimum edge costs
        all_costs = sorted(list(set(cost for _, _, cost in edges)))
        
        if not can_reach_with_min_cost(0):
            return -1
            
        low = 0
        high = len(all_costs) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            threshold = all_costs[mid]
            
            if can_reach_with_min_cost(threshold):
                ans = threshold
                low = mid + 1
            else:
                high = mid - 1
                
        return ans