from algorithms.constants import NODE_TYPE

class Node():
    def __init__(self, row, column, width, total_rows):
        self.row = row
        self.column = column
        self.width = width
        self.x = row * width
        self.y = column * width
        self.total_rows = total_rows
        self.node_type = 'default'
        self.neighbors = list()

    def get_position(self):
        '''
        returns node position in pygame window
        '''
        return self.row, self.column
    
    def is_type(self, node_type='default'):
        '''
        compares node type to target type
        '''
        return self.node_type == node_type
    
    def make_type(self, node_type='default'):
        '''
        change node type to target type
        '''
        self.node_type = node_type
    
    def draw(self, draw, window):
        '''
        draw node in pygame window
        '''
        draw(window, NODE_TYPE[self.node_type], (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        '''
        checks non-diagonal neighbors to verify neighbor is not a node of type barrier
        
        is barrier : ignore neighbor
        is not barrier: add neighbor to node object's neighbors list
        '''

        self.neighbors = list()

        # check neighbor left of current node
        if self.column > 0:
            left_neighbor = grid[self.row][self.column - 1]
            if not left_neighbor.is_type('barrier') and not left_neighbor.is_type('wall'):
                self.neighbors.append(left_neighbor)
        
        # check neighbor below current node
        if self.row < self.total_rows - 1:
            bottom_neighbor = grid[self.row + 1][self.column]
            if not bottom_neighbor.is_type('barrier') and not bottom_neighbor.is_type('wall'):
                self.neighbors.append(bottom_neighbor)

        # check neighbor right of current node
        if self.column < self.total_rows - 1:
            right_neighbor = grid[self.row][self.column + 1]
            if not right_neighbor.is_type('barrier') and not right_neighbor.is_type('wall'):
                self.neighbors.append(right_neighbor)

        # check neighbor above current node
        if self.row > 0:
            top_neighbor = grid[self.row - 1][self.column]
            if not top_neighbor.is_type('barrier') and not top_neighbor.is_type('wall'):
                self.neighbors.append(top_neighbor)

    def __lt__(self, other):
        return False