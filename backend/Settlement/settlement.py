from collections import namedtuple
from enum import Enum

Settlement = namedtuple('Settlement', [
    'name',
    'outboundRoads',
    'stock'
])

class SettlementIds(Enum):
    JAMAICA_PLAIN = 1
    PARK_STREET = 2
    GOODNEIGHBOR = 3
    DIAMOND_CITY = 4