# **Path Finding Algorithm Visualizer With Python**

Visualize pathfinding algorithms with the option to select from diffrent algorithms

***

## **Description**

Allows for the visualization of the following pathfinding algorithms:

#### **Breadth First Search**

* **Algorithm**
    1. initialize queue, insert source node to queue
    2. while queue is not empty
        * generate current node's neighborhood and set their previous as the current node
        * for each neighbor
            1. if neighbor is target, stop search
            2. set neighbor to visted
            3. insert all unvisited neighbours into queue

* **Time Complexity**
    * O(V+E), where V is the number of vertices and E is the number of edges in the graph

* **Space Complexity**
    * O(V), where V is the total number of vertices

#### **Depth First Search**

* **Algorithm**
    1. initialize stack, push source node to stack
    2. while stack is not empty
        * generate current node's neighborhood and set their previous as the current node
        * for each neighbor
            1. if neighbor is target, stop search
            2. set neighbor to visted
            3. if a neighbor is set to visted and it currently has unvisted neighbors push neighbor to stack
            4. if a neighbor is set to the visted and it currently has no unvisted neighbors, remove neighbor from neighborhood
        * if current node has no univisted neighbors pop from stack

* **Time Complexity**
    * O(V+E), where V is the number of vertices and E is the number of edges in the graph

* **Space Complexity**
    * O(V), where V is the total number of vertices

#### **Disjsktra**

* **Algorithms**
    1. initialize priority queue, push source node to queue
    2. assign a distance value to all vertices,
       initialize all distance values as inf, assign
       the distance value as 0 for the source vertex
    3. while queue is not empty
        * find open node with minimum distance value
           an set it to current node
        * set current node to closed
        * generate current node's neighborhood and set their
           previous as the current node
        * for each neighbor
            1. if neighbor is target, stop search
            2. else, compute distance value for each neighbor
                * neighbor distance = current node distance + distance between current and neighbor
            3. if a neighbor is set to open and its current distance value is lower than the new distance value, skip the neighbor
            4. if a neighbor is set to the closed and its current distance value is lower than the new distance value, skip the neighbor otherwise, set the neighbor to the open
        * set neighbor to closed

* **Time Complexity**
    * priority queue version (above implementation)
        * O(E logV), where V is the total number of vertices and E is the number of edges in the graph
    * adjacency list version
        * O(V^2), where V is the total number of vertices

* **Space Complexity**
    * O(V), where V is the total number of vertices

#### **A Star**

* **Algorithms**
    1. initialize priority queue, push source node to queue
    2. while queue is not empty
        * find open node with least f score an set it to current node
        * set current node to closed
        * generate current node's neighborhood and set their previous as the current node
        * for each neighbor
            1. if neighbor is target, stop search
            2. else, compute g score, f score, and manhattan distance for each neighbor
                * neighbor g score = current g score + manhattan distance between neighbor and current node
                * neighbor manhattan distance = distance from target to neighbor
                * neighbor f score = neighbor g score + neighbor manhattan distance
            3. if a neighbor is set to open and its current f score is lower than the new f score, skip the neighbor
            4. if a neighbor is set to the closed and its current f score is lower than the new f score, skip the neighbor otherwise, set the neighbor to the open
        * set neighbor to closed

* **Time Complexity**
    * O(E), where E is the number of edges in the graph

* **Space Complexity**
    * O(V), where V is the total number of vertices

***

### **Technologies**

[Python](https://www.python.org/) : 3.9.1

[Pygame](https://www.pygame.org/news) : 2.1.2

***

## **Installation**

***

```
$ git clone https://github.com/justin-h-mills/Pathfinding_Algorithm_Visualizer_With_Python.git
$ sudo apt-get install python3-pygame
```

***

## **User Guide**

***

**Syntax**

```Python
from visualizer import Visualizer

'''
algorithm options
    - BreadthFirst (default)
    - DepthFirst
    - Dijsktra
    - A*
'''

algorithm = 'A*'

visualizer = Visualizer(algorithm)

# starts running visualizer with selected algorithm
visualizer.start_visualization()

algorithm = 'DepthFirst'

# change algorithm visualizer uses after creation
visualizer.algorithm_selection(algorithm)
```

**Visualizer Controls**

* left click
    * at mouse position
        1. adds source node to grid
        2. if source on grid, add target node to grid
        3. if both source and target on grid, add wall node to grid
* right click
    * at mouse position
        * remove source, target, or wall node from grid
* spacebar
    * if source and target node are on grid start running selected pathfinding algorithm
* c
    * before or after pathfinding algorithm has run
        * clear grid of source, target, and wall node from grid

***

## **Resources**

***

[A* Pathfinding Visualization Tutorial](https://www.youtube.com/watch?v=JtiK0DOeI4A)

[A* Search Algorithm](https://www.geeksforgeeks.org/a-search-algorithm/)

[Dijkstra's Shortest Path Algorithm](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)

[The ultimate introduction to Pygame](https://www.youtube.com/watch?v=AY9MnQ4x3zk)

[Breadth First Search or BFS for a Graph](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)

[Depth First Search or DFS for a Graph](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)

***

## **License**

***

MIT License

Copyright (c) [2022]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.