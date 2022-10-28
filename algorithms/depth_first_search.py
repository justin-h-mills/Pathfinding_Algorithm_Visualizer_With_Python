
class DepthFirst():
    def __init__(self):
        self.prev_node = {}
    
    def get_next_neighbor(self, current):
        '''
        get non-visited neighbor from current nodes neighborhood
        '''

        # check if current node has neighbors
        if current.neighbors:
            # find neighbor that hasn't been visited yet
            for neighbor in current.neighbors:
                if not neighbor.is_type('open') and not neighbor.is_type('source'):
                    neighbor.make_type('open')
                    return neighbor

    def build_path(self, stack, target):
        '''
        empty stack into prev_node for path generation
        '''
        current = target
        while stack:
            prev = stack.pop()
            self.prev_node[current] = prev
            current = prev

    def run(self, draw, source, target, event_quit, grid):
        '''
        find if path exists using depth first search algorithm
        '''
        stack = [source]
        current = source

        while stack:
            event_quit()

            neighbor = self.get_next_neighbor(current)
            
            if neighbor == target:
                self.build_path(stack, target)
                return True
            
            if neighbor and neighbor.neighbors and neighbor.is_type('open'):
                stack.append(neighbor)
                current = neighbor
            elif neighbor and not neighbor.neighbors and neighbor.is_type('open'):
                current.neighbors.remove(neighbor)
                current = stack.pop()
            else:
                current = stack.pop()

            current.make_type('current')
            draw()
            current.make_type('open')
        
        return False
    
'''
Depth First Search Algorithm
    1. initialize stack, push source node to stack
    2. while stack is not empty
        a. generate current node's neighborhood and set their
           previous as the current node
        b. for each neighbor
            i. if neighbor is target, stop search
            ii. set neighbor to visted
            iii. if a neighbor is set to visted and it currently has unvisted neighbors
                push neighbor to stack
            iv. if a neighbor is set to the visted and it currently has no unvisted neighbors,
                remove neighbor from neighborhood
        c. if current node has no univisted neighbors pop from stack

Depth First Search Time Complexity
    - O(V+E), where V is the number of vertices
      and E is the number of edges in the graph

Depth First Search Space Complexity
    - O(V), where V is the total number of vertices
'''