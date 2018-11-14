from collections import defaultdict, namedtuple

###################################
#Data definitions
###################################
Settlement = namedtuple('Settlement', [
    'name',
    'neighbors',
    'stock'
])

CommerceItem = namedtuple('CommerceItem', [
    'name',
    'price'
])

Edge = namedtuple('Edge', ['dest', 'cost'])

###################################
# Instances
###################################

# Create some blank settlements to be filled in during world creation.
settlements = {
    'Jamaica Plain': Settlement('Jamaica Plain', [], {}),
    'Park Street': Settlement('Park Street', [], {}),
    'Goodneighbor': Settlement('Goodneighbor', [], {}),
    'Diamond City': Settlement('Diamond City', [], {}),
}

edges = [
    ('Jamaica Plain', 'Diamond City', 3),
    ('Park Street', 'Diamond City', 1),
    ('Goodneighbor', 'Diamond City', 1)
]

###################################
#Functions
###################################

def connect_the_dots(settlements, edges):
    for origin, dest, cost in edges:
        # Create a doubly-linked path from Settlement A to B
        settlements[origin].neighbors.append(Edge(dest, cost))
        settlements[dest].neighbors.append(Edge(origin, cost))
    return settlements

def init_commerce_items(settlements):
    for name in settlements:
        settlements[name].stock['Jet'] = CommerceItem('Jet', 300)
        settlements[name].stock['Psycho'] = CommerceItem('Psycho', 1200)
    return settlements

def pprint(settlements):
    for name, settlement in settlements.items():
        print(name)

        for edge in settlement.neighbors:
            print(f'\t-> {edge.dest} ({edge.cost})')

        for key, chem in settlement.stock.items():
            print(f'\t\t {chem.name} @ {chem.price} caps')


###################################
# Do it!
###################################
pprint(init_commerce_items(
    connect_the_dots(
        settlements, edges)))
