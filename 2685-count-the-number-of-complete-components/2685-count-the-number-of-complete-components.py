class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        complete_components_count = 0
        for i in range(n):
            if not visited[i]:
                # Initialize BFS
                queue = deque([i])
                visited[i] = True
                component_vertices = []
                while queue:
                    curr = queue.popleft()
                    component_vertices.append(curr)
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                v_count = len(component_vertices)
                is_complete = True
                for vertex in component_vertices:
                    if len(adj[vertex]) != v_count - 1:
                        is_complete = False
                        break
                if is_complete:
                    complete_components_count += 1
        return complete_components_count