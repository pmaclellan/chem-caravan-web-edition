import unittest
from World import World, tick

class TickMethodTests(unittest.TestCase):
    def test_initial_state(self):
        w = World()
        self.assertEqual(w.time, 0)

    def test_tick_increments_time_by_one(self):
        w = World()
        w = tick(w)
        self.assertEqual(w.time, 1)

if __name__ == '__main__':
    unittest.main()