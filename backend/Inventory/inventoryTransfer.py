from inventory import Inventory
from counter import incrementingCounter
from collections import namedtuple

Removal = namedtuple('Removal', ['ItemId', 'InventoryId'])
Addition =  namedtuple('Addition', ['Item', 'InventoryId'])

class InventoryTransfer:
   def __init__(self, inventories):
      self.idGenerator = incrementingCounter()
      self.inventories = {}
      self.pendingRemovals = []
      self.pendingAdditions = []
      # Assign an ID to each inventory
      for inventory in inventories:
         self.inventories[self.idGenerator.__next__()] = inventory

   def StageMove(self, itemId, fromInventory, toInventory):
      if fromInventory not in self.inventories:
         raise ValueError('From inventory is not part of this transfer')
      if toInventory not in self.inventories:
         raise ValueError('To inventory is not part of this transfer')
      if itemId not in self.inventories[fromInventory].items:
         raise ValueError('Provided item not found in inventory')

      item = self.inventories[fromInventory].items[itemId]

      self.pendingAdditions.append(Addition(item, toInventory))
      self.pendingRemovals.append(Removal(itemId, fromInventory))

   def Commit(self):
      # Perform the removals first to clear up space
      for removal in self.pendingRemovals:
         self.inventories[removal.InventoryId].Remove(removal.ItemId)
      
      for addition in self.pendingAdditions:
         self.inventories[addition.InventoryId].Add(addition.Item)

      return tuple(self.inventories.values())