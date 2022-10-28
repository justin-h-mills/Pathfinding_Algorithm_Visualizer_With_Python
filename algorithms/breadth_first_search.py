from collections import deque

class BreadthFirst():
    def __init__(self):
        self.prev_node = {}
    
    def get_neighborhood(self, current, queue):
        '''
        get non-visited neighbor from current nodes neighborhood
        '''

        # check if current node has neighbors
        if current.neighbors:
            # find neighbor that hasn't been visited yet
            for neighbor in current.neighbors:
                if not neighbor.is_type('open') and not neighbor.is_type('source'):
                    neighbor.make_type('open')
                    queue.append(neighbor)
                    self.prev_node[neighbor] = current

    def run(self, draw, source, target, event_quit, grid):
        '''
        find if path exists using depth first search algorithm
        '''
        queue = deque()
        queue.append(source)
        current = source

        while queue:
            event_quit()

            self.get_neighborhood(current, queue)

            neighbor = queue.popleft()

            if neighbor == target:
                return True

            current = neighbor

            current.make_type('current')
            draw()
            current.make_type('open')
        
        return False
    
'''
Breadth First Search Algorithm
    1. initialize queue, insert source node to queue
    2. while queue is not empty
        a. generate current node's neighborhood and set their
           previous as the current node
        b. for each neighbor
            i. if neighbor is target, stop search
            ii. set neighbor to visted
            iii. insert all unvisited neighbours into queue

Breadth First Search Time Complexity
    - O(V+E), where V is the number of vertices
      and E is the number of edges in the graph

Breadth First Search Space Complexity
    - O(V), where V is the total number of vertices
'''