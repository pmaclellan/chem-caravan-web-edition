from collections import defaultdict, namedtuple

from Settlement.settlement import Settlement, SettlementIds
from CommerceItem.commerceItem import CommerceItem
from Road.road import Road, RoadIds

###################################
# Database tables
###################################

blank_settlements = {
    SettlementIds.JAMAICA_PLAIN: Settlement('Jamaica Plain', [], {}),
    SettlementIds.PARK_STREET: Settlement('Park Street', [], {}),
    SettlementIds.GOODNEIGHBOR: Settlement('Goodneighbor', [], {}),
    SettlementIds.DIAMOND_CITY: Settlement('Diamond City', [], {}),
}

roads = {
    RoadIds.RIVERWAY: Road(SettlementIds.JAMAICA_PLAIN, SettlementIds.DIAMOND_CITY, 3),
    RoadIds.BOYLSTON: Road(SettlementIds.PARK_STREET, SettlementIds.DIAMOND_CITY, 1),
    RoadIds.MASS_AVE: Road(SettlementIds.GOODNEIGHBOR, SettlementIds.PARK_STREET, 1)
}

###################################
#Functions
###################################

def connect_the_dots(settlements, roads):
    for roadId, road in roads.items():
        # Create a doubly-linked path from Settlement A to B
        settlements[road.origin].outboundRoads.append(roadId)
        settlements[road.dest].outboundRoads.append(roadId)
    return settlements

def init_commerce_items(settlements):
    for name in settlements:
        settlements[name].stock['Jet'] = CommerceItem('Jet', 300)
        settlements[name].stock['Psycho'] = CommerceItem('Psycho', 1200)
    return settlements

def pprint(settlements):
    for settlementId, settlement in settlements.items():
        print(settlement.name)

        for key, chem in settlement.stock.items():
            print(f'  {chem.name} @ {chem.price} caps')

        for roadId in settlement.outboundRoads:
            print(f'\t-> {roads[roadId].dest} ({roads[roadId].cost})')

        print('\n')

###################################
# Do it!
###################################
pprint(init_commerce_items(
    connect_the_dots(
        blank_settlements, roads)))
