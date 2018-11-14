from collections import namedtuple
from enum import Enum

'''
    A Road is a directed path from one Settlement to
    another that has an associated cost to travel on.
'''
Road = namedtuple('Road', ['origin', 'dest', 'cost'])

class RoadIds(Enum):
    RIVERWAY = 1
    BOYLSTON = 2
    MASS_AVE = 3