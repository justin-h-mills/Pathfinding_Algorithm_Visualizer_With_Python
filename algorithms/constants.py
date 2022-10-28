from algorithms.a_star_search import A_Star
from algorithms.dijsktra_search import Dijsktra
from algorithms.depth_first_search import DepthFirst
from algorithms.breadth_first_search import BreadthFirst

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

NODE_TYPE = {
    'closed' : RED,
    'open' : GREEN,
    'default' : WHITE,
    'barrier' : BLACK,
    'path' : PURPLE,
    'source' : ORANGE,
    'target' : TURQUOISE,
    'wall' : BLACK,
    'current' : BLUE
}

COLOR = {
    'white' : WHITE,
    'grey' : GREY
}

ALGORITHM = {
    'A*' : A_Star(),
    'Dijsktra' : Dijsktra(),
    'DepthFirst' : DepthFirst(),
    'BreadthFirst' : BreadthFirst()
}