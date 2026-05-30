import bisect

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return max(p1, p2)


class Solution:
    def getResults(self, queries):
        # Determine the maximum coordinate bounding box dynamically
        max_x = max(q[1] for q in queries)
        n = max_x + 1
        
        st = SegmentTree(n)
        obstacles = [0]
        results = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                # Find insertion position for x
                idx = bisect.bisect_right(obstacles, x)
                prev_obs = obstacles[idx - 1]
                
                # Update the segment tree for the newly created gap at x
                st.update(1, 0, n - 1, x, x - prev_obs)
                
                # If there's a subsequent obstacle, shrink its existing gap
                if idx < len(obstacles):
                    next_obs = obstacles[idx]
                    st.update(1, 0, n - 1, next_obs, next_obs - x)
                
                # Insert the obstacle to keep the list sorted
                obstacles.insert(idx, x)
                
            else:
                x, sz = q[1], q[2]
                # Find the largest obstacle <= x
                idx = bisect.bisect_right(obstacles, x)
                prev_obs = obstacles[idx - 1]
                
                # 1. Get the max gap entirely to the left of prev_obs
                max_gap = st.query(1, 0, n - 1, 0, prev_obs)
                
                # 2. Get the dangling partial gap up to x
                max_gap = max(max_gap, x - prev_obs)
                
                results.append(max_gap >= sz)
                
        return results