# Inventory Management
## State of the Module
This module gives us a basic inventory management system. You can instantiate\
an Inventory object, add and remove items from it, and check its total capacity\
and currently used space. Further, you can set up a Transfer session with one\
or more inventories. This allows you to trade items between the inventories in\
sets of commit. within a given commit inventory sizes are ignored to allow\
trading between inventories that are full without having to shuffle things\
around in an annoying way.

Overall it should be a workable version 1. We can add more features and\
refactor it later once we know more about the rest of the system.

## Future Improvements
* Allow player to "drop" items. This will come into play when they find a body\
with something valuable on it and want to drop their less valuable items to\
free up space.
* Add the concept of Inventory sets to the transfers. This will come into play\
for trading with merchants. We want to consider the collective goods and money\
of all members in the caravan on one side and the merchant's goods and money\
on the other side.