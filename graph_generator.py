import random

class GraphGenerator:
    """
    GraphGenerator provides methods to create Hamiltonian and non-Hamiltonian undirected graphs
    with specified edge saturation (density).
    """

    def generate_hamiltonian_graph(self, n, saturation):
        """
        Generate a connected undirected Hamiltonian graph on n vertices with approx given saturation (%).
        Ensures there is a Hamilton cycle and all vertex degrees are even.
        Note: final saturation may slightly exceed target due to parity fixes.
        """
        if n <= 10:
            raise ValueError("Number of vertices must be > 10 for Hamiltonian graph generation.")

        # Initialize empty adjacency list
        graph = {i: set() for i in range(n)}
        # Create a random Hamilton cycle
        cycle = list(range(n))
        random.shuffle(cycle)
        for i in range(n):
            u = cycle[i]
            v = cycle[(i + 1) % n]
            graph[u].add(v)
            graph[v].add(u)
        current_edges = n

        # Compute target number of edges
        max_edges = n * (n - 1) // 2
        target_edges = int(max_edges * saturation / 100)

        # Add random edges until reaching target saturation
        attempts = 0
        max_attempts = (target_edges - current_edges) * 20
        while current_edges < target_edges and attempts < max_attempts:
            u, v = random.sample(range(n), 2)
            if v not in graph[u]:
                graph[u].add(v)
                graph[v].add(u)
                current_edges += 1
            attempts += 1

        # Fix any odd-degree vertices by adding edges (will increase edge count if needed)
        self._ensure_even_degrees(graph)
        return graph

    def _ensure_even_degrees(self, graph):
        """
        Fix vertices with odd degree by pairing them:
        - If two odd vertices u, v are not adjacent, add edge (u,v).
        - Otherwise, add a two-edge path u-w-v via a third vertex w.
        Repeat until no odd-degree vertices remain.
        """
        odd = [v for v in graph if len(graph[v]) % 2 == 1]
        while len(odd) >= 2:
            u = odd.pop()
            v = odd.pop()
            if v not in graph[u]:
                graph[u].add(v)
                graph[v].add(u)
            else:
                # find third vertex w
                w_candidates = [w for w in graph if w not in (u, v) and w not in graph[u] and w not in graph[v]]
                if w_candidates:
                    w = random.choice(w_candidates)
                    graph[u].add(w); graph[w].add(u)
                    graph[v].add(w); graph[w].add(v)
                else:
                    # fallback: pair u with any odd vertex not tested
                    for x in odd:
                        if x not in graph[u]:
                            graph[u].add(x)
                            graph[x].add(u)
                            odd.remove(x)
                            break
            odd = [v for v in graph if len(graph[v]) % 2 == 1]

    def generate_non_hamiltonian_graph(self, n):
        """
        Generate an undirected non-Hamiltonian graph on n vertices
        at approx 50% edge saturation by isolating one vertex.
        Isolation of a vertex ensures no Hamilton cycle.
        """
        if n <= 1:
            raise ValueError("Need at least 2 vertices for non-Hamiltonian graph.")

        graph = {i: set() for i in range(n)}
        max_edges = n * (n - 1) // 2
        target_edges = int(max_edges * 50 / 100)

        # choose isolated vertex to break Hamiltonicity
        isolated = random.randrange(n)
        others = [v for v in range(n) if v != isolated]
        possible_edges = [(u, v) for i, u in enumerate(others) for v in others[i+1:]]

        # add edges randomly until target
        random.shuffle(possible_edges)
        for u, v in possible_edges:
            if len(graph[u]) + len(graph[v]) >= n - 2:
                # avoid creating a new Hamilton cycle by high-degree vertices; optional
                pass
            graph[u].add(v)
            graph[v].add(u)
            if sum(len(adj) for adj in graph.values()) // 2 >= target_edges:
                break

        return graph

