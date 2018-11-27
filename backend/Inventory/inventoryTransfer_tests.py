import unittest
from inventory import Inventory, InventoryItem
from inventoryTransfer import InventoryTransfer, InvalidTransactionWarning

# Define global test InventoryItem's
jet1 = InventoryItem('Jet', 1)
jet2 = InventoryItem('Jet', 1)
mirelurkMeat1 = InventoryItem('Mirelurk Meat', 3)
mirelurkMeat2 = InventoryItem('Mirelurk Meat', 3)
weapon1 = InventoryItem('Alien Blaster', 5)

# Create some test Inventory's
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

    def test_transfer_with_no_inventories_is_error(self):
        '''Reject transfer between zero inventories'''
        with self.assertRaises(ValueError):
            transfer = InventoryTransfer([])

    def test_move_invalid_item_raises_error(self):
        '''Reject moving an item that is not present in the 'from' Inventory.'''
        transfer = InventoryTransfer([inventory1, inventory2])
        with self.assertRaises(ValueError):
            transfer.StageMove(9999, 0, 1)

    def test_invalid_inventory_raises_error(self):
        '''Reject move to an inventory that doesn't exist in this transfer.'''
        invalidInventoryId = 2 # Because there are only [0,1]
        transfer = InventoryTransfer([inventory1, inventory2])
        with self.assertRaises(ValueError):
            transfer.StageMove(jet1Id, 0, 2)

    def test_move_one_item_and_commit(self):
        transfer = InventoryTransfer([inventory1, inventory2])
        transfer.StageMove(jet1Id, 0, 1) # 0 is inventory1, 1 is inventory2
        # Commit the transaction and check that the item was moved
        inv1, inv2 = transfer.Commit()
        self.assertIn(jet1, inv2.items.values(),
            'Item was not added to inventory')
        self.assertNotIn(jet1, inv1.items.values(),
            'Item was not removed from inventory')

    def test_move_then_move_back(self):
        pass

    def test_cannot_exceeed_capacity(self):
        transfer = InventoryTransfer([inventory1, inventory2])
        transfer.StageMove(mirelurk2Id, 1, 0) # 0 is inventory1, 1 is inventory2
        with self.assertRaises(InvalidTransactionWarning):
            transfer.Commit()
        
        # Check that we rolled back the inventories after a bad commit
        self.assertEqual(inventory1, transfer.inventories[0])
        self.assertEqual(inventory2, transfer.inventories[1])

if __name__ == '__main__':
    unittest.main()