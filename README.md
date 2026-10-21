# SC2001 – Algorithm Design and Analysis

This repository contains the implementations, experiments, and analyses developed for **SC2001: Algorithm Design and Analysis** at Nanyang Technological University (NTU), Singapore.

The projects explore algorithm design techniques, theoretical complexity, empirical performance evaluation, and optimisation.

## Projects Overview

| Project | Topic | Focus |
|---|---|---|
| Project 1 | Hybrid Sorting Algorithm | Merge Sort, Insertion Sort, and performance optimisation |
| Project 2 | Dijkstra's Shortest Path Algorithm | Adjacency Matrix vs Adjacency List with Binary Heap |
| Project 3 | Dynamic Programming | Unbounded Knapsack Problem and subproblem dependencies |

---

## Project 1 – Hybrid Sorting Algorithm

### Objective

Implement and evaluate a hybrid sorting algorithm that combines **Merge Sort and Insertion Sort**, using a threshold value `S` to improve sorting efficiency for smaller subarrays.

### Implementation

- Implement standard Merge Sort and Insertion Sort.
- Develop a hybrid sorting algorithm that switches to Insertion Sort when the subarray size is at most `S`.
- Analyse the number of key comparisons for different input sizes and threshold values.
- Measure CPU execution time to identify an efficient threshold.
- Compare the hybrid algorithm against standard Merge Sort.

### Analysis

The experiments investigate how input size and threshold selection influence the algorithm's performance, using both key comparisons and execution time.

### Key Files

- `sorts.cpp` – Sorting algorithm implementations
- `sorts_tester.cpp`, `sorts_tester2.cpp` – Testing and verification
- `partB_data_generator.cpp` – Input data generation
- `partCi_hybrid_analysis.cpp` – Hybrid sorting analysis
- `partCii_hybrid_analysis.cpp` – Threshold comparison analysis
- `partCiii_hybrid_analysis.cpp` – CPU time analysis
- `graphs_generation.py` – Experimental graph generation

---

## Project 2 – Dijkstra's Shortest Path Algorithm

### Objective

Implement Dijkstra's shortest path algorithm using two graph representations and compare their theoretical and empirical performance.

### Part A – Adjacency Matrix

Implement Dijkstra's algorithm using an **Adjacency Matrix** and a linear scan to select the next minimum-distance vertex.

**Time Complexity:** `O(V²)`

### Part B – Adjacency List with Binary Heap

Implement Dijkstra's algorithm using an **Adjacency List** and a Binary Min-Heap priority queue.

**Time Complexity:** `O((V + E) log V)`

### Part C – Performance Comparison

Compare the two implementations using graphs with different numbers of vertices and edges.

The experiments examine:

- Sparse and dense graph structures
- Execution time as the number of vertices increases
- Execution time as the number of edges increases
- The relationship between graph representation and algorithm performance

### Key Files

**Part A**
- `dijkstra_matrix.cpp` – Adjacency Matrix implementation
- `benchmark_matrix.cpp` – Performance benchmarking
- `check_correctness.cpp` – Correctness verification
- `plot_matrix_results.py` – Results visualisation

**Part B**
- `dijkstra_heap.cpp` – Adjacency List and Binary Heap implementation
- `benchmark_heap.cpp` – Performance benchmarking

**Part C**
- `graph_comparison.ipynb` – Comparative analysis and visualisation

---

## Project 3 – Dynamic Programming: Unbounded Knapsack

### Objective

Solve the **Unbounded Knapsack Problem** using dynamic programming.

Given a knapsack of capacity `C` and `n` object types, each with a positive integer weight and profit, determine the maximum achievable profit without exceeding the capacity.

An unlimited number of copies of each object type is available.

### Part 1 – Recursive Definition

Define `P(C)` as the maximum profit obtainable with knapsack capacity `C`.

The recurrence considers every object that fits, adds its profit to the optimal profit for the remaining capacity, and selects the maximum.

If no object fits, the maximum additional profit is zero.

### Part 2 – Subproblem Graph

Construct a directed subproblem graph for `P(15)` using:

| Object | Weight | Profit |
|---|---:|---:|
| 1 | 4 | 7 |
| 2 | 5 | 6 |
| 3 | 8 | 9 |

Each node represents a unique subproblem, while directed edges represent dependencies between larger and smaller capacities.

The graph is generated programmatically using Python, NetworkX, and Graphviz.

**Files**
- `part1/recursive_definition.md` – Recursive definition and explanation
- `part2/subproblem_graph.py` – Graph generation script
- `part2/subproblem_graph.dot` – Graphviz graph definition
- `part2/subproblem_graph.png` – Generated subproblem graph

### Parts 3 and 4 – Pending Integration

- **Part 3:** Bottom-up dynamic programming algorithm
- **Part 4:** Implementation and results for the specified knapsack test cases

These sections will be updated as the remaining group contributions are integrated.

---

## Repository Structure

```text
SC2001-Projects/
├── Project 1/
│   ├── data/
│   ├── sorts.cpp
│   ├── sorts_tester.cpp
│   ├── sorts_tester2.cpp
│   ├── partB_data_generator.cpp
│   ├── partCi_hybrid_analysis.cpp
│   ├── partCii_hybrid_analysis.cpp
│   ├── partCiii_hybrid_analysis.cpp
│   └── graphs_generation.py
│
├── Project 2/
│   ├── datasets/
│   ├── part_a/
│   ├── part_b/
│   └── part_c/
│
├── Project 3/
│   ├── part1/
│   │   └── recursive_definition.md
│   └── part2/
│       ├── subproblem_graph.py
│       ├── subproblem_graph.dot
│       └── subproblem_graph.png
│
└── README.md
```

## Technologies Used

- **C++** – Algorithm implementation and performance benchmarking
- **Python** – Data analysis, testing, and visualisation
- **NetworkX** – Graph construction
- **Graphviz** – Directed graph visualisation
- **Git and GitHub** – Version control and collaboration

## Getting Started

Clone the repository:

```bash
git clone https://github.com/gangadv1/SC2001-Projects.git
cd SC2001-Projects
```

### C++ Programs

Compile an individual C++ source file using a C++17-compatible compiler. For example:

```bash
g++ -std=c++17 -O2 "Project 1/sorts.cpp" -c
```

Individual experiments may require additional source files or specific execution arguments.

### Project 3 – Generate the Subproblem Graph

Install the required Python dependency:

```bash
python3 -m pip install networkx
```

Install Graphviz separately. On macOS with Homebrew:

```bash
brew install graphviz
```

Generate the graph:

```bash
python3 "Project 3/part2/subproblem_graph.py"
```

The generated image will be saved as:

`Project 3/part2/subproblem_graph.png`

---

## Learning Outcomes

Across the three projects, the repository demonstrates:

- Implementation and analysis of fundamental algorithms
- Evaluation of time complexity and empirical performance
- Understanding algorithmic trade-offs across different data structures
- Application of dynamic programming to optimisation problems
- Experimental benchmarking and results visualisation
- Collaborative software development using Git and GitHub

---

**Course:** SC2001 – Algorithm Design and Analysis  
**Institution:** Nanyang Technological University, Singapore
