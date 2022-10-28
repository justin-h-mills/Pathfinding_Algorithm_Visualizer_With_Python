from queue import PriorityQueue

class A_Star():
    def __init__(self) -> None:
        self.prev_node = {}
        
    def manhattan_distance(self, current, target):
        '''
        calculates the manhattan distance between the current
        node and the end node
        '''
        x1, y1 = current
        x2, y2 = target
        return abs(x1 - x2) + abs(y1 - y2)

    def run(self, draw, source, target, event_quit, grid):
        '''
        search graph for shortest path between source and target node using
        A* Search algorithm
        '''
        priority = 0

        # create priority queue and add source node to head with initial priority value
        open_set = PriorityQueue()
        open_set.put((0, priority, source))

        # set each nodes g_score to default value and the source node to its initial value
        g_score = {node: float('inf') for row in grid for node in row}
        g_score[source] = 0

        # set each nodes f_score to default value and the source node to its initial value
        f_score = {node: float('inf') for row in grid for node in row}
        f_score[source] = self.manhattan_distance(source.get_position(),
                                                  target.get_position())

        # add source to node tracking dictionary
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
            
            # search node neighborhood and calculate g and f score for each neighbor
            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    self.prev_node[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + self.manhattan_distance(neighbor.get_position(),
                                                                               target.get_position())
                    if neighbor not in open_set_hash:
                        priority += 1
                        open_set.put((f_score[neighbor], priority, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_type('open')
        
            # mark node as searched
            if current != source:
                current.make_type('closed')
            
            # redraw pygame window
            draw()

        
        return False

'''
A* Search Algorithm
    1. initialize priority queue, push source node to queue
    2. while queue is not empty
        a. find open node with least f score an set it to current node
        b. set current node to closed
        c. generate current node's neighborhood and set their
           previous as the current node
        d. for each neighbor
            i. if neighbor is target, stop search
            ii. else, compute g score, f score, and manhattan distance
                for each neighbor
                    - neighbor g score = current g score + manhattan
                      distance between neighbor and current node
                    - neighbor manhattan distance = distance from target
                      to neighbor
                    - neighbor f score = neighbor g score + neighbor manhattan distance
            iii. if a neighbor is set to open and its current f score is lower
                 than the new f score, skip the neighbor
            iv. if a neighbor is set to the closed and its current f score is lower
                than the new f score, skip the neighbor otherwise, set the neighbor
                to the open
        e. set neighbor to closed

A* Search Time Complexity
    - O(E), where E is the number of edges in the graph

A* Search Space Complexity
    - O(V), where V is the total number of vertices
'''