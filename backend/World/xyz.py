from collections import defaultdict, namedtuple

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

# Create some blank settlements to be filled in during world creation.
settlements = {
    'Jamaica Plain': Settlement('Jamaica Plain', [], None),
    'Park Street': Settlement('Park Street', [], None),
    'Goodneighbor': Settlement('Goodneighbor', [], None),
    'Diamond City': Settlement('Diamond City', [], None),
}

edges = [
    ('Jamaica Plain', 'Diamond City', 3),
    ('Park Street', 'Diamond City', 1),
    ('Goodneighbor', 'Diamond City', 1)
]

def connect_the_dots(settlements, edges):
    for origin, dest, cost in edges:
        # Create a doubly-linked path from Settlement A to B
        settlements[origin].neighbors.append(Edge(dest, cost))
        settlements[dest].neighbors.append(Edge(origin, cost))
    return settlements

def make_world(edges):
    world = defaultdict(set)
    for origin, destination, cost in edges:
        world[origin].add(Edge(destination, cost))
        world[destination].add(Edge(origin, cost))
    return world

def pprint(settlements):
    for name, settlement in settlements.items():
        print(name)
        for edge in settlement.neighbors:
            print(f'\t-> {edge.dest} ({edge.cost})')

pprint(connect_the_dots(settlements, edges))
#pprint(make_world(edges))
