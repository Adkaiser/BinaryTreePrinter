from BinaryTreeParser import BinaryTreeParser, EMPTYNODESTRING

class BinaryNode:
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None
	
	def getVal(self):
		return self.value
	
	def getNode(self, side):
		return getattr(self, side, False)
	
	#To ensurej that nodes are not overwritten, we will only permit this if there is no node already on the specified side
	def setNode(self, side, val):
		if(self.getNode(side)):
			return False
		newnode = BinaryNode(val)
		setattr(self, side, newnode)
		return True
		
root = BinaryNode(1)
root.setNode("left", 3)
root.setNode("right", 15)
root.getNode("left").setNode("left", 6)
root.getNode("left").setNode("right", 8)
root.getNode("right").setNode("left", 2)
root.getNode("right").setNode("right", 9)
parser = BinaryTreeParser(root, "value", "left", "right")
assert parser.parseTree() == [1, 3, 15, 6, 8, 2, 9]

root = BinaryNode(1)
root.setNode("right", 15)
root.getNode("right").setNode("left", 2)
root.getNode("right").setNode("right", 9)
parser = BinaryTreeParser(root, "value", "left", "right")
assert parser.parseTree() == [1, EMPTYNODESTRING, 15, EMPTYNODESTRING, EMPTYNODESTRING, 2, 9]