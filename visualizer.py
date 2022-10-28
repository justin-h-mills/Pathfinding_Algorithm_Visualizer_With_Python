from algorithms.constants import COLOR
from algorithms.pathfinding_algorithm import PATHFINDING_ALGORITHM

import pygame


class Visualizer():
    def __init__(self, algorithm='BreadthFirst'):
        self.width = 600
        self.rows = 50
        self.gap = self.width // self.rows
        self.pathfinding = PATHFINDING_ALGORITHM(self.rows, self.width, self.gap, algorithm)
        self.window = pygame.display.set_mode((self.width, self.width))
        self.source = None
        self.target = None
        pygame.display.set_caption('Path Finding Algorithm Visualizer')

    def algorithm_selection(self, algorithm):
        self.pathfinding.set_algorithm(algorithm)
        return algorithm
    
    def draw_grid(self):
        '''
        draw pathfinding grid overlay in window
        '''
        for i in range(self.rows):
            pygame.draw.line(self.window, COLOR['grey'],
                             (0, i * self.gap),
                             (self.width, i * self.gap))

            for j in range(self.rows):
                pygame.draw.line(self.window, COLOR['grey'],
                                 (j * self.gap, 0),
                                 (j * self.gap, self.width))

    def draw(self):
        '''
        draw nodes into pathfinding grid
        '''
        self.window.fill(COLOR['white'])

        if self.source:
            self.source.make_type('source')
        if self.target:
            self.target.make_type('target')

        for row in self.pathfinding.grid:
            for node in row:
                node.draw(pygame.draw.rect, self.window)
        
        self.draw_grid()
        pygame.display.update()
    
    def get_mouse_position(self, position):
        '''
        returns position of mouse in window
        '''
        position_y, position_x = position

        row = position_y // self.gap
        column = position_x // self.gap

        return row, column

    def event_quit(self, event=None):
        '''
        closes window when quit event occurs
        '''
        if event == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        else:
            if event.type == pygame.QUIT:
                    return False
        return True

    def event_left_click(self):
        '''
        updates node types source, target, or barrier when left click event occurs
        '''
        position = pygame.mouse.get_pos()
        row, column = self.get_mouse_position(position)
        node = self.pathfinding.grid[row][column]

        if not self.source and node != self.target and not node.is_type('wall'):
            self.source = node
            self.source.make_type('source')
        elif not self.target and node != self.source and not node.is_type('wall'):
            self.target = node
            self.target.make_type('target')
        elif node != self.target and node != self.source and not node.is_type('wall'):
            node.make_type('barrier')

    def event_right_click(self):
        '''
        resets node type to default when right click event occurs
        '''
        position = pygame.mouse.get_pos()
        row, column = self.get_mouse_position(position)
        node = self.pathfinding.grid[row][column]

        if node.is_type('source'):
            node.make_type('default')
            self.source = None
        elif node.is_type('target'):
            node.make_type('default')
            self.target = None
        elif node.is_type('barrier'): 
            node.make_type('default')

    def event_mouse_click(self):
        '''
        checks for mouse click event occurence
        '''
        if pygame.mouse.get_pressed()[0]:
            self.event_left_click()
        elif pygame.mouse.get_pressed()[2]:
            self.event_right_click()

    

    def event_keydown_space(self):
        '''
        start running pathfinding algorithm when keydown space event occurs
        '''
        for row in self.pathfinding.grid:
            for node in row:
                node.update_neighbors(self.pathfinding.grid)
                
        self.pathfinding.run(self.draw,
                             self.source,
                             self.target,
                             self.event_quit)

    def event_keydown_c(self):
        '''
        reset all node types to default when keydown c event occurs
        '''
        self.pathfinding.reset_grid()
        self.source = None
        self.target = None
    
    def event_keydown(self, event):
        '''
        checks for keydown event occurence
        '''
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE and self.source and self.target:
                self.event_keydown_space()
            if event.key == pygame.K_c:
                self.event_keydown_c()

    def start_visualization(self):
        '''
        starts pathfinding visualization
        '''
        self.draw()

        run = True

        while run:
            self.draw()
            for event in pygame.event.get():
                run = self.event_quit(event)
                self.event_mouse_click()
                self.event_keydown(event)
        
        pygame.quit()
    
    def update_algorithm(self, algorithm):
        '''
        allows user to change pathfinding algorithm
        being used by the visualizer
        '''
        self.pathfinding.set_algorithm(algorithm)
        return algorithm