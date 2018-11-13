from collections import defaultdict, namedtuple

Edge = namedtuple('Edge', ['dest', 'cost'])

edges = [
    ('Jamaica Plain', 'Diamond City', 3),
    ('Park Street', 'Diamond City', 1),
    ('Goodneighbor', 'Diamond City', 1)]

def make_world(edges):
    world = defaultdict(set)
    for origin, destination, cost in edges:
        world[origin].add(Edge(destination, cost))
        world[destination].add(Edge(origin, cost))
    return world

def pprint(world):
    for location, edges in world.items():
        print(location)
        for edge in edges:
            print(f'\t-> {edge.dest} ({edge.cost})')

pprint(make_world(edges))