
import subprocess
from pathlib import Path

import networkx as nx

# Given data from Part (2)
weights = [4, 5, 8]
profits = [7, 6, 9]
capacity = 15

graph = nx.DiGraph()
visited = set()


def build_graph(c):
    if c in visited:
        return

    visited.add(c)
    graph.add_node(c)

    for weight, profit in zip(weights, profits):
        if weight <= c:
            remaining = c - weight

            graph.add_edge(
                c,
                remaining,
                label=f"w={weight}, p={profit}"
            )

            build_graph(remaining)


build_graph(capacity)

# Generate a Graphviz DOT file
output_dir = Path(__file__).resolve().parent
dot_file = output_dir / "subproblem_graph.dot"
png_file = output_dir / "subproblem_graph.png"

with dot_file.open("w") as f:
    f.write("digraph SubproblemGraph {\n")
    f.write('  graph [rankdir=TB, nodesep=0.8, ranksep=1.1];\n')
    f.write('  node [shape=ellipse, style=filled, fillcolor=lightblue];\n')
    f.write('  edge [fontsize=10];\n')

    for c in sorted(graph.nodes(), reverse=True):
        f.write(f'  {c} [label="P({c})"];\n')

    for u, v, data in graph.edges(data=True):
        f.write(f'  {u} -> {v} [label="{data["label"]}"];\n')

    f.write("}\n")

# Render the DOT file as a PNG
subprocess.run(
    ["dot", "-Tpng", str(dot_file), "-o", str(png_file)],
    check=True
)

print(f"Graph generated: {png_file}")
print(f"Total unique subproblems: {graph.number_of_nodes()}")
print(f"Total dependencies: {graph.number_of_edges()}")
