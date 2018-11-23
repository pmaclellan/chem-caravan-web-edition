import unittest
from inventory import Inventory, InventoryItem
from inventoryTransfer import InventoryTransfer

# Define global test objects
jet1 = InventoryItem('Jet', 1)
jet2 = InventoryItem('Jet', 1)
mirelurkMeat1 = InventoryItem('Mirelurk Meat', 3)
mirelurkMeat2 = InventoryItem('Mirelurk Meat', 3)
weapon1 = InventoryItem('Alien Blaster', 5)

# Inventory 1 is at max capcity
inventory1 = Inventory(10)
weapon1Id = inventory1.Add(weapon1)
mirelurk1Id = inventory1.Add(mirelurkMeat1)
jet1Id = inventory1.Add(jet1)
jet2Id = inventory1.Add(jet2)

# Inventory 2 is 1 under capacity
inventory2 = Inventory(4)
mirelurk2Id = inventory2.Add(mirelurkMeat2)

class InventoryTransferTests(unittest.TestCase):
   def test_transfer_with_no_inventories(self):
      transfer = InventoryTransfer([])

   def test_move_invalid_item_raises_error(self):
      transfer = InventoryTransfer([inventory1, inventory2])
      with self.assertRaises(ValueError):
         transfer.StageMove(9999, 0, 1)

   def test_invalid_inventory_raises_error(self):
      transfer = InventoryTransfer([inventory1, inventory2])
      with self.assertRaises(ValueError):
         transfer.StageMove(jet1Id, 0, 2)

   def test_move_one_item_and_commit(self):
      transfer = InventoryTransfer([inventory1, inventory2])
      transfer.StageMove(jet1Id, 0, 1) # 0 is inventory1, 1 is inventory2
      # Commit the transaction and check that the item was moved
      inv1, inv2 = transfer.Commit()
      print(inv1.items)
      print(inv2.items)
      self.assertIn(jet1, inv2.items.values(),
         'Item was not added to inventory')
      self.assertNotIn(jet1, inv1.items.values(),
         'Item was not removed from inventory')

if __name__ == '__main__':
    unittest.main()