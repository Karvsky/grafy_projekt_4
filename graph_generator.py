import random

class GraphGenerator:
    
    def generate_hamiltonian_graph(self, n, saturation):
        graph = {i: set() for i in range(n)}
        
        hamilton_cycle = list(range(n))
        random.shuffle(hamilton_cycle)
        
        for i in range(n):
            current = hamilton_cycle[i]
            next_vertex = hamilton_cycle[(i + 1) % n]
            graph[current].add(next_vertex)
            graph[next_vertex].add(current)
        
        max_edges = n * (n - 1) // 2
        current_edges = n
        target_edges = int(max_edges * saturation / 100)
        
        attempts = 0
        max_attempts = target_edges * 10
        
        while current_edges < target_edges and attempts < max_attempts:
            v1, v2 = random.sample(range(n), 2)
            if v2 not in graph[v1]:
                graph[v1].add(v2)
                graph[v2].add(v1)
                current_edges += 1
            attempts += 1
        
        self._ensure_even_degrees(graph, n)
        return graph
    
    def _ensure_even_degrees(self, graph, n):
        odd_vertices = []
        for v in range(n):
            if len(graph[v]) % 2 == 1:
                odd_vertices.append(v)
        
        while len(odd_vertices) >= 2:
            v1 = odd_vertices.pop()
            v2 = odd_vertices.pop()
            
            if v2 not in graph[v1]:
                graph[v1].add(v2)
                graph[v2].add(v1)
            else:
                available = []
                for v3 in range(n):
                    if v3 != v1 and v3 != v2 and v3 not in graph[v1] and v3 not in graph[v2]:
                        available.append(v3)
                
                if available:
                    v3 = random.choice(available)
                    graph[v1].add(v3)
                    graph[v3].add(v1)
                    graph[v2].add(v3)
                    graph[v3].add(v2)
                    if len(graph[v3]) % 2 == 1:
                        odd_vertices.append(v3)
    
    def _add_random_cycle(self, graph, n):
        cycle_length = random.choice([3, 4])
        available_vertices = list(range(n))
        cycle_vertices = random.sample(available_vertices, cycle_length)
        
        for i in range(cycle_length):
            v1 = cycle_vertices[i]
            v2 = cycle_vertices[(i + 1) % cycle_length]
            if v2 not in graph[v1]:
                graph[v1].add(v2)
                graph[v2].add(v1)
    
    def generate_non_hamiltonian_graph(self, n):
        graph = {i: set() for i in range(n)}
        
        hamilton_cycle = list(range(n))
        random.shuffle(hamilton_cycle)
        
        for i in range(n):
            current = hamilton_cycle[i]
            next_vertex = hamilton_cycle[(i + 1) % n]
            graph[current].add(next_vertex)
            graph[next_vertex].add(current)
        
        max_edges = n * (n - 1) // 2
        current_edges = n
        target_edges = int(max_edges * 50 / 100)
        
        attempts = 0
        max_attempts = target_edges * 10
        
        while current_edges < target_edges and attempts < max_attempts:
            v1, v2 = random.sample(range(n), 2)
            if v2 not in graph[v1]:
                graph[v1].add(v2)
                graph[v2].add(v1)
                current_edges += 1
            attempts += 1
        
        self._ensure_even_degrees(graph, n)
        
        isolated_vertex = random.choice(range(n))
        neighbors = list(graph[isolated_vertex])
        for neighbor in neighbors:
            graph[isolated_vertex].remove(neighbor)
            graph[neighbor].remove(isolated_vertex)
        
        return graph