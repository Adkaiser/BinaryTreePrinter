#Code to build and validate a BST.
#Assumes unbalanced, multiple equivalent values on the right side

#Node for the tree. Thanks to the factory, the node will not contain any Binary Search logic
class BSTNode:
	
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None
	
	def getVal(self):
		return self.value
	
	def getNode(self, side):
		return getattr(self, side, False)
	
	#To ensurej that nodes are not overwritten, we will only permit this if there is no node already on the specified side
	def setNode(self, newnode, side):
		if(self.getNode(side)):
			return False
		setattr(self, side, newnode)
		return True
		
		
class BSTFactory:
	
	def __init__(self):
		self.root = False
	
	def add(self, val):
		newnode = BSTNode(val)
		#If tree has no root, this is now the root.
		if not self.root:
			self.root = BSTNode(val)
		#Otherwise, find its place in the tree with a recursive search
		else:
			self.addToNode(self.root, val, newnode)
	
	def addToNode(self, node, val, newnode):
		#Determine which side the new value should go on
		if val < node.getVal():
			side = "left"
		else:
			side = "right"
		#Try to set the node. We'll get False if there's already a node there.
		sidenode = node.setNode(newnode, side)
		#If we got False, recurse
		if not sidenode:
			self.addToNode(node.getNode(side), val, newnode)
			
	def getRoot(self):
		return self.root
		 
	def retrieveBST(self):
		final_list = self.printNode(self.root)
		return final_list
				
	def printBST(self):
		print self.retrieveBST()
			
	def printNode(self, node):
		leftnode = node.getNode("left")
		if leftnode:
			val_list = self.printNode(leftnode)
		else:
			val_list = []
		val_list.append(node.getVal())
		rightnode = node.getNode("right")
		if rightnode:
			val_list += self.printNode(rightnode)
		return val_list
		
	def validateBST(self):
		values = self.retrieveBST()
		print values == sorted(values)