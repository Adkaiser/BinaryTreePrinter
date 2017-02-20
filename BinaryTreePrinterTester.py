from BinaryTreePrinter import printBinaryTree
from BSTFactory import BSTFactory

printBinaryTree([1, 2, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
printBinaryTree([1, 2.8, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
printBinaryTree([10, 2, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
printBinaryTree([10, 2.8, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
printBinaryTree([100, 2, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
printBinaryTree([1000, 2, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "


		
tree = BSTFactory()
tree.add(4.5)
tree.add(7)
tree.add(2)
tree.add(6)
tree.add(1)

printBinaryTree(tree.getRoot(), "value", "left", "right")
print " "
print " "