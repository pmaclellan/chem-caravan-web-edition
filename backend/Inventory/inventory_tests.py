import unittest
from inventory import Inventory, InventoryItem

class InventoryTests(unittest.TestCase):
   def test_initial_state(self):
        inv = Inventory(10)
        self.assertEqual(inv.capacity, 10)

   def test_can_add_to_empty(self):
      inv = Inventory(10)
      self.assertNotEqual(None, inv.Add(InventoryItem('Foo', 2)))

   def test_cannot_add_over_capacity(self):
      inv = Inventory(1)
      self.assertFalse(inv.Add(InventoryItem('Two Heavy', 2)))

   def test_current_weight_updated_after_add(self):
      inv = Inventory(10)
      #Check the starting weight
      self.assertEqual(0, inv.currentWeight)
      inv.Add(InventoryItem('Three\'s company', 3))
      #Check the weight after adding
      self.assertEqual(3, inv.currentWeight)

   def test_can_get_added_item(self):
      inv = Inventory(10)
      myItem = InventoryItem('MyHelloWorldInventoryItem', 3)
      inv.Add(myItem)
      self.assertIn(myItem, inv.items.values())

   def test_can_remove_item_by_id(self):
      inv = Inventory(10)
      item = InventoryItem('Throwaway InventoryItem #1', 1)
      itemId = inv.Add(item)
      self.assertEqual(item, inv.Remove(itemId))

   def test_remove_nonexistatnt_item_id(self):
      inv = Inventory(4)
      nonExistantItemId = 1
      self.assertEqual(None, inv.Remove(nonExistantItemId))

   def test_remove_opens_space(self):
      inv = Inventory(4)
      item1 = InventoryItem('Big fatty', 3)
      item2 = InventoryItem('Little guy', 2)
      itemId1 = inv.Add(item1)
      # Check that we can't add item2 becuase there is not enough space
      self.assertEqual(None, inv.Add(item2))
      # Now remove item1 and check that we can add item2
      inv.Remove(itemId1)
      self.assertNotEqual(None, inv.Add(item2))

if __name__ == '__main__':
    unittest.main()