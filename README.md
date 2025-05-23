# Impression Network Analysis

This repository contains three Python programs and their corresponding documents that analyze a social impression network derived from `impression_2.csv`. These programs help in identifying leaders, discovering missing links, and evaluating centrality metrics like betweenness and clustering coefficients.

## 📁 Files Overview

### 1. `Question_1.py` - **Finding the Leader**
- **Objective:** To find the most influential person (leader) using a random walk with teleportation method.
- **Approach:**
  - Simulates 1,000,000 random walks on the impression data.
  - Uses a teleportation probability of 15% to ensure exploration even in disconnected subgraphs.
  - Counts visit frequencies to determine node influence.
- **Documentation:** See `question_1.pdf` for explanation and methodology.

---

### 2. `Question_2.py` - **Finding the Missing Links**
- **Objective:** To predict potential missing links in the network using linear regression.
- **Approach:**
  - Constructs an adjacency matrix from the CSV.
  - Applies matrix regression on 0-entries to decide whether to add a new edge.
  - Recalculates PageRank before and after edge additions to observe changes.
- **Key Insight:** Adds edges where inferred connection value > 0.5.
- **Documentation:** See `Question_2.pdf` for detailed logic and explanation.

---

### 3. `Question_3.py` - **Betweenness and Clustering Coefficient**
- **Objective:** To evaluate the structural importance and cohesion of each node.
- **Metrics:**
  - **Betweenness Centrality:** Identifies nodes acting as bridges in the network.
  - **Clustering Coefficient:** Measures how close a node's neighbors are to forming a clique.
- **Output:** Lists nodes ranked by both metrics.
- **Documentation:** See `Question_3.pdf` for concept details and their real-world significance.

---

## 📊 Dataset

### `impression_2.csv`

This file represents a real dataset collected from students on our campus. Each student was asked to list the top 30 individuals they felt most connected to or impressed by.  
- **Column Format:** Each row starts with the student's own identifier (e.g., email or entry number), followed by up to 30 other identifiers.
- **Interpretation:** An edge from student A to student B means A listed B in their top 30.
- This forms the basis of a **directed graph** used for analysis in the provided Python scripts.

---

## 🧠 Author

**Asodariya Harsh**  
Entry Number: 2023csb1103  
Indian Institute of Technology Ropar

---

## 🔧 Requirements

- Python 3.x
- `pandas`
- `numpy`
- `networkx`

Install dependencies with:
```bash
pip install pandas numpy networkx
