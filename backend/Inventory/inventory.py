from counter import incrementingCounter

class Inventory:
   '''
   An Inventory is a thin wrapper around a collection of items. Each item has a
   weight that counts towards the Inventory's overall capacity. Items are
   tracked with unique IDs
   '''
   def __init__(self, capacity: int):
      self.capacity = capacity
      self.currentWeight = 0
      self.items = {}
      self.idGenerator = incrementingCounter()

   def Add(self, item):
      # Only add if we have space available
      if self.currentWeight + item.weight <= self.capacity:
         self.currentWeight += item.weight
         # Generate a new ID
         itemId = self.idGenerator.__next__()
         self.items[itemId] = item
         return itemId
      
      return None

   def Remove(self, itemId):
      # Pull out the item if it exists
      removedItem = self.items.pop(itemId, None)
      if removedItem != None:
         self.currentWeight -= removedItem.weight
      
      return removedItem

class InventoryItem:
   def __init__(self, name, weight):
      self.name = name
      self.weight = weight

   def __repr__(self):
      return f'{self.name}: weight {self.weight}'