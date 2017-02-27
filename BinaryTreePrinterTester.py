from BinaryTreePrinter import printBinaryTree
from BSTFactory import BSTFactory

#Single digits
printBinaryTree([1, 2, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
#Decimals
printBinaryTree([1, 2.8, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
#Two digits
printBinaryTree([10, 2, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
#Two digits and decimals
printBinaryTree([10, 2.8, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
#More than two digits
printBinaryTree([100, 2, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
printBinaryTree([1000, 2, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
#Negatives
printBinaryTree([-1, 2, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
printBinaryTree([-1, 2.3, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
printBinaryTree([-1.4, 2.3, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])
print " "
print " "
#File printing
printBinaryTree([10, 2, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 7, 8, 9, 1, 1, 1, 2, 3, 4, 7, 8, 9, 1, 1, 1, 2, 3, 4, 3, 4, 7, 130], file="test.txt")


		
tree = BSTFactory()
tree.add(4.5)
tree.add(7)
tree.add(2)
tree.add(6)
tree.add(1)

printBinaryTree(tree.getRoot(), "value", "left", "right")
print " "
print " "

printBinaryTree(tree.getRoot(), "value", "left", "right", file="bsttest.txt")
print " "
print " "

printBinaryTree("jsontest1.json", "value", "left", "right")
print " "
print " "