import copy

class GraphOperations:
    
    def __init__(self, graph):
        self.graph = graph
    
    def print_graph(self):
        print("\nGraph representation (adjacency list):")
        
        max_vertex_width = max(len(str(v)) for v in self.graph.keys()) if self.graph else 1
        max_neighbors_width = max(len(str(sorted(list(self.graph[v])))) for v in self.graph.keys()) if self.graph else 1
        max_degree_width = max(len(str(len(self.graph[v]))) for v in self.graph.keys()) if self.graph else 1
        
        for vertex in sorted(self.graph.keys()):
            neighbors = sorted(list(self.graph[vertex]))
            degree = len(neighbors)
            parity = "even" if degree % 2 == 0 else "odd"
            
            vertex_str = str(vertex).ljust(max_vertex_width)
            neighbors_str = str(neighbors).ljust(max_neighbors_width)
            degree_str = str(degree).ljust(max_degree_width)
            
            print(f"{vertex_str}: {neighbors_str} (degree: {degree_str}, {parity})")
        
        edges = []
        for v in self.graph:
            for neighbor in self.graph[v]:
                if (neighbor, v) not in edges:
                    edges.append((v, neighbor))
        
        print(f"\nTotal nodes: {len(self.graph)}")
        print(f"Total edges: {len(edges)}")
        
        odd_degree_count = sum(1 for v in self.graph if len(self.graph[v]) % 2 == 1)
        print(f"Nodes with odd degree: {odd_degree_count}\n")
    
    def find_euler_cycle(self):
        if not self._has_euler_cycle():
            return None
        
        graph_copy = copy.deepcopy(self.graph)
        
        non_empty_vertices = [v for v in graph_copy if graph_copy[v]]
        if not non_empty_vertices:
            return []
        
        start_vertex = non_empty_vertices[0]
        circuit = []
        stack = [start_vertex]
        
        while stack:
            curr = stack[-1]
            if graph_copy[curr]:
                next_vertex = graph_copy[curr].pop()
                graph_copy[next_vertex].remove(curr)
                stack.append(next_vertex)
            else:
                circuit.append(stack.pop())
        
        return circuit[::-1] if len(circuit) > 1 else None
    
    def _has_euler_cycle(self):
        non_empty_vertices = [v for v in self.graph if self.graph[v]]
        if not non_empty_vertices:
            return False
        
        if not self._is_connected(non_empty_vertices):
            return False
        
        for vertex in self.graph:
            if len(self.graph[vertex]) % 2 != 0:
                return False
        
        return True
    
    def _is_connected(self, vertices):
        if not vertices:
            return True
        
        start = vertices[0]
        visited = set()
        stack = [start]
        
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                for neighbor in self.graph[v]:
                    if neighbor in vertices and neighbor not in visited:
                        stack.append(neighbor)
        
        return len(visited) == len(vertices)
    
    def find_hamilton_cycle(self):
        n = len(self.graph)
        if n == 0:
            return None
            
        start_vertex = min(self.graph.keys())
        path = [start_vertex]
        visited = {start_vertex}
        
        if self._hamilton_backtrack(path, visited, n):
            return path + [start_vertex]
        return None
    
    def _hamilton_backtrack(self, path, visited, n):
        if len(path) == n:
            start_vertex = path[0]
            return start_vertex in self.graph[path[-1]]
        
        current_vertex = path[-1]
        
        for next_vertex in sorted(self.graph[current_vertex]):
            if next_vertex not in visited:
                path.append(next_vertex)
                visited.add(next_vertex)
                
                if self._hamilton_backtrack(path, visited, n):
                    return True
                
                path.pop()
                visited.remove(next_vertex)
        
        return False