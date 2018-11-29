import unittest
from inventory import Inventory, InventoryItem

class InventoryTests(unittest.TestCase):

    def test_initial_capacity(self):
        '''Properly initialize the capacity of a new inventory.'''
        inv = Inventory(10)
        self.assertEqual(inv.capacity, 10)

    def test_can_add_to_empty(self):
        '''
        We can add an item to an inventory with sufficient space
        available and get back an item ID.
        '''
        inv = Inventory(10)
        self.assertNotEqual(None, inv.Add(InventoryItem('Foo', 2)))

    def test_cannot_add_over_capacity_empty(self):
        '''
        We get a ValueError if we try to add an item that is larger
        than the inventory's capacity and thus whill not fit.
        '''
        inv = Inventory(1)
        with self.assertRaises(ValueError):
            inv.Add(InventoryItem('Two Heavy', 2))

    def test_cannot_add_over_capacity_partially_filled(self):
        '''
        We get a ValueError if we try to add an item that will not
        fit in the inventory because there are already other items.
        '''
        inv = Inventory(3)
        first = InventoryItem('the worst', 2)
        second = InventoryItem('the best', 2)
        inv.Add(first) # This should work just fine
        with self.assertRaises(ValueError):
            inv.Add(second)

    def test_current_weight_updated_after_add(self):
        '''
        Inventory.currentWeight gets updated as expected when a new
        item is added successfully.
        '''
        inv = Inventory(10)
        #Check the starting weight
        self.assertEqual(0, inv.currentWeight)
        inv.Add(InventoryItem('Three\'s company', 3))
        #Check the weight after adding
        self.assertEqual(3, inv.currentWeight)

    def test_can_get_added_item(self):
        '''
        Check that we can retrieve an item we added using the ID that
        was returned by Add.
        '''
        inv = Inventory(10)
        myItem = InventoryItem('MyHelloWorldItem', 3)
        myId = inv.Add(myItem)
        self.assertEqual(myItem, inv.items.get(myId))

    def test_can_remove_item_by_id(self):
        '''
        Removing an item using the ID returned by Add should remove
        it from the inventory and return the item.
        '''
        inv = Inventory(10)
        item = InventoryItem('Throwaway InventoryItem #1', 1)
        itemId = inv.Add(item)
        self.assertEqual(item, inv.Remove(itemId))
        self.assertNotIn(item, inv.items.items())

    def test_remove_nonexistatnt_item_id(self):
        '''
        Trying to remove a non-existant item ID should do nothing
        and return None.
        '''
        inv = Inventory(4)
        nonExistantItemId = 1
        self.assertEqual(None, inv.Remove(nonExistantItemId))

    def test_remove_opens_space(self):
        '''
        If an Add fails due to insufficient capacity, we should be able
        to remove an item to make space and then Add the original item.
        '''
        inv = Inventory(4)
        item1 = InventoryItem('Big fatty', 3)
        item2 = InventoryItem('Little guy', 2)
        itemId1 = inv.Add(item1)
        # Check that we can't add item2 becuase there is not enough space
        with self.assertRaises(ValueError):
            inv.Add(item2)
        # Now remove item1 and check that we can add item2
        inv.Remove(itemId1)
        self.assertNotEqual(None, inv.Add(item2))

if __name__ == '__main__':
    unittest.main()