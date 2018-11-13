from dataclasses import dataclass

@dataclass
class World:
    time: int =0

def tick(world):
    world.time += 1
    return world
