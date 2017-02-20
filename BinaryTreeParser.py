from Queue import Queue

class BinaryTreeParser:
	def __init__(self, root, val, left, right):
		self.root = root
		self.queue = Queue(0)
		self.valproperty = val
		self.leftproperty = left
		self.rightproperty = right
		
	def parseTree(self):
		#Ensure properties defined for BT node object are present
		if not self.valproperty or not self.leftproperty or not self.rightproperty:
			raise ValueError("Properties of binary node object are not defined.")
		for key, prop in dict.iteritems({"node value": self.valproperty, "left node": self.leftproperty, "right node": self.rightproperty}):
			if not hasattr(self.root, prop):
				raise  ValueError("Binary tree node object doesn't contain the specified property for the " + key + ". Given property name: "+prop)
		
		arraytree = []
		#Start the queue
		self.queue.put(self.root)
		#Parse the value of every node into the array, using Breadth-First Searching
		while not self.queue.empty():
			node = self.queue.get()
			arraytree.append(getattr(node, self.valproperty))
			if getattr(node, self.leftproperty, False):
				self.queue.put(getattr(node, self.leftproperty))
			if getattr(node, self.rightproperty, False):
				self.queue.put(getattr(node, self.rightproperty))
		
		return arraytree