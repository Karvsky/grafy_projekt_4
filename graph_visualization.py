import math

def export_to_tikz(graph, filename="graph.tex", radius=3):
    n = len(graph)
    if n == 0:
        print("Graph is empty, nothing to export")
        return

    verts = sorted(graph.keys())
    coords = {}
    for i, v in enumerate(verts):
        angle = 2 * math.pi * i / n
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        coords[v] = (x, y)

    with open(filename, "w") as f:
        f.write("\\begin{tikzpicture}[scale=1, every node/.style={circle,draw}]\n")
        for v, (x, y) in coords.items():
            f.write(f"  \\node (N{v}) at ({x:.2f},{y:.2f}) {{{v}}};\n")
        f.write("\n")
        for u in verts:
            for v in sorted(graph[u]):
                if (v,u) in seen:
                    continue
                f.write(f"  \\draw (N{u}) -- (N{v});\n")
                seen.add((u,v))
        f.write("\\end{tikzpicture}\n")

if __name__ == "__main__":
    import sys
    from graph_operations import GraphOperations
    sample = {1:{2,3}, 2:{1,3}, 3:{1,2}}
    export_to_tikz(sample, filename=sys.argv[1] if len(sys.argv)>1 else "graph.tex")