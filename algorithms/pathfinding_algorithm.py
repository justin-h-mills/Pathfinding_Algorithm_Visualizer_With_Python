from algorithms.constants import ALGORITHM
from algorithms.node import Node

class PATHFINDING_ALGORITHM():
    def __init__(self, rows, width, gap, algorithm):
        self.rows = rows
        self.width = width
        self.gap = gap
        self.grid = self.make_grid()
        self.algorithm = ALGORITHM[algorithm]

    def set_algorithm(self, algorithm):
        self.algorithm = ALGORITHM[algorithm]
        return algorithm

    def make_grid(self):
        '''
        creates grid for pathfinding algorithm with each grid
        place holding a object of type node
        '''
        grid = list()

        for i in range(self.rows):
            grid.append(list())
            for j in range(self.rows):
                node = Node(i, j, self.gap, self.rows)

                if i + 2 >= self.rows or j + 2 >= self.rows or i <=1 or j <=1:
                    node.make_type('wall')

                grid[i].append(node)
        
        return grid
    
    def reset_grid(self):
        '''
        sets all node objects in grid to their default node type
        '''
        for row in self.grid:
            for node in row:
                if not node.is_type('wall'):
                    node.make_type('default')
    
    def reconstruct_path(self, prev_node, current, draw):
        '''
        change all nodes in shortest path to nodes of type
        path and draw node to pygame window
        '''
        current.make_type('target')

        while current in prev_node:
            current = prev_node[current]
            if not current.is_type('source') and not current.is_type('target'):
                current.make_type('path')
            elif current.is_type('source'):
                break
                        
            draw()
    
    def run(self, draw, source, target, event_quit):
        '''
        executes pathfinding algorithm and reconstruct shortest path if found
        '''
        if self.algorithm.run(draw, source, target, event_quit, self.grid):
            source.make_type('source')
            target.make_type('target')
            self.reconstruct_path(self.algorithm.prev_node, target, draw)
            return True
        return False