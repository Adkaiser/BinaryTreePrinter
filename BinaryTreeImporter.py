class BTNode:
	
	def __init__(self, nodeval, valueprop, leftprop, rightprop):
		setattr(self, valueprop, nodeval)
		setattr(self, leftprop, None)
		setattr(self, rightprop, None)
		
		#Reflect the user-defined property names into the function to create a new child node
		def setSideNode(side, node):
			if not getattr(self, side):
				setattr(self, side, node)
				
		setattr(self, "setSideNode", setSideNode)
		
def parseFromString(filedir, value="value", left="left", right="right"):
	dirparts = filedir.split(".")
	if dirparts[-1] == "json":
		return readJSONFile(filedir, value, left, right)
	#elif dirparts[-1] == "xml":
	#	return readXMLFile(filedir, value, left, right)

def readJSONFile(filedir, value, left, right):
	import json
	with open(filedir) as openfile:
		jsondata = json.load(openfile)
		
	root = parseJSONSet(jsondata, value, left, right)
	return root
	
def parseJSONSet(jsonset, value, left, right):
	if value in jsonset:
		newNode = BTNode(jsonset[value], value, left, right)
		#Look for a node to put on either side
		sides = [left, right]
		for side in sides:
			if side in jsonset and isinstance(jsonset[side], dict):
				newNode.setSideNode(side, parseJSONSet(jsonset[side], value, left, right))
		return newNode
	return None
	
	