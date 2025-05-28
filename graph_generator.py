import random

class GraphGenerator:

    def generate_hamiltonian_graph(self, n, saturation):
        if n <= 10:
            raise ValueError("Number of vertices must be > 10 for Hamiltonian graph generation.")

        graph = {i: set() for i in range(n)}
        cycle = list(range(n))
        random.shuffle(cycle)
        for i in range(n):
            u = cycle[i]
            v = cycle[(i + 1) % n]
            graph[u].add(v)
            graph[v].add(u)
        current_edges = n

        max_edges = n * (n - 1) // 2
        target_edges = int(max_edges * saturation / 100)

        attempts = 0
        max_attempts = (target_edges - current_edges) * 20
        while current_edges < target_edges and attempts < max_attempts:
            u, v = random.sample(range(n), 2)
            if v not in graph[u]:
                graph[u].add(v)
                graph[v].add(u)
                current_edges += 1
            attempts += 1

        self._ensure_even_degrees(graph)
        return graph

    def _ensure_even_degrees(self, graph):
        odd = [v for v in graph if len(graph[v]) % 2 == 1]
        while len(odd) >= 2:
            u = odd.pop()
            v = odd.pop()
            if v not in graph[u]:
                graph[u].add(v)
                graph[v].add(u)
            else:
                w_candidates = [w for w in graph if w not in (u, v) and w not in graph[u] and w not in graph[v]]
                if w_candidates:
                    w = random.choice(w_candidates)
                    graph[u].add(w); graph[w].add(u)
                    graph[v].add(w); graph[w].add(v)
                else:
                    for x in odd:
                        if x not in graph[u]:
                            graph[u].add(x)
                            graph[x].add(u)
                            odd.remove(x)
                            break
            odd = [v for v in graph if len(graph[v]) % 2 == 1]

    def generate_non_hamiltonian_graph(self, n):
        if n <= 1:
            raise ValueError("Need at least 2 vertices for non-Hamiltonian graph.")

        graph = {i: set() for i in range(n)}
        max_edges = n * (n - 1) // 2
        target_edges = int(max_edges * 50 / 100)

        isolated = random.randrange(n)
        others = [v for v in range(n) if v != isolated]
        possible_edges = [(u, v) for i, u in enumerate(others) for v in others[i+1:]]

        random.shuffle(possible_edges)
        for u, v in possible_edges:
            if len(graph[u]) + len(graph[v]) >= n - 2:
                pass
            graph[u].add(v)
            graph[v].add(u)
            if sum(len(adj) for adj in graph.values()) // 2 >= target_edges:
                break

        return graph

