from queue import PriorityQueue

class Dijsktra():
    def __init__(self):
        self.prev_node = {}

    def run(self, draw, source, target, event_quit, grid):
        '''
        search graph for shortest path between source and target node using
        Dijsktra Search algorithm
        '''
        priority = 0

        # create priority queue and add source node to head with initial priority value
        open_set = PriorityQueue()
        open_set.put((0, priority, source))

        # set each nodes distance to default value and the source node to its initial value
        distance = {node: float('inf') for row in grid for node in row}
        distance[source] = 0

        # add start to node tracking dictionary
        open_set_hash = {source}

        # start pathfinding
        while not open_set.empty():
            # allows user to close pygame window while algorithm is running
            event_quit()

            # get next node to search
            current = open_set.get()[2]
            open_set_hash.remove(current)

            # check if shortest path found
            if current == target:
                return True
            
            # search node neighborhood and calculate distance value for each neighbor
            for neighbor in current.neighbors:
                temp_distance = distance[current]

                if temp_distance < distance[neighbor]:
                    self.prev_node[neighbor] = current
                    distance[neighbor] = temp_distance + 1
                    if neighbor not in open_set_hash:
                        priority += 1
                        open_set.put((distance[neighbor], priority, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_type('open')
        
            # mark node as searched
            if current != source:
                current.make_type('closed')
            
            # redraw pygame window
            draw()
        
        return False
'''
Dijsktra Search Algorithm
    1. initialize priority queue, push source node to queue
    2. assign a distance value to all vertices,
       initialize all distance values as inf, assign
       the distance value as 0 for the source vertex
    3. while queue is not empty
        a. find open node with minimum distance value
           an set it to current node
        b. set current node to closed
        c. generate current node's neighborhood and set their
           previous as the current node
        d. for each neighbor
            i. if neighbor is target, stop search
            ii. else, compute distance value for each neighbor
                - neighbor distance = current node distance + distance between
                  current and neighbor
            iii. if a neighbor is set to open and its current distance value is lower
                 than the new distance value, skip the neighbor
            iv. if a neighbor is set to the closed and its current distance value is 
                lower than the new distance value, skip the neighbor otherwise, set
                the neighbor to the open
        e. set neighbor to closed

Dijsktra Search Time Complexity
    - priority queue version (above implementation)
        - O(E logV), where V is the total number of vertices
          and E is the number of edges in the graph
    - adjacency list version
        - O(V^2), where V is the total number of vertices

Dijsktra Search Space Complexity
    - O(V), where V is the total number of vertices
'''