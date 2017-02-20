from math import log, ceil, floor

def printBinaryTree(tree, valProp=None, leftProp=None, rightProp=None):
	#If already an array, print array
	if isinstance(tree, list):
		printArrayTree(tree)
		
	#If object-based, parse tree into array based on properties passed to function

def printArrayTree(tree):
	#Find number of layers of tree, which equals log(base2) x
	layers = int(ceil(log(len(tree) + 1, 2)))
	currentlayer = 0
	offset = 0
	#Find the largest number that we'll have to deal with
	largest = max(map(lambda x: str(x), tree), key=len)
	digits = len(str(largest))
	
	#Adjust formatting based on digit length.
	if digits % 2 == 0:
		branchspace = 4
		numindent = 2-int(floor(digits/2))
		branchfactor = lambda x: x-2
	else:
		branchspace = 3
		numindent = 1-int(floor(digits/2))
		branchfactor = lambda x: x-1
	
	#Find starting spacing
	spacing = branchspace
	for i in range(layers-1):
		spacing = spacing * 2 + digits
	
	#Recurse through each layer
	while currentlayer < layers:
		#The bottom layer will always have a smaller indent
		indent = findIndent(layers, currentlayer, digits, branchspace, numindent)
		
		#Print current layer
		layerString = " " * indent
		if 2**currentlayer > len(tree):
			layerarray = tree[offset:]
		else:
			layerarray = tree[offset:2**currentlayer+offset]
		for i, val in enumerate(layerarray):
			if i != 0:
				layerString += " " * spacing
				
			#Determine number formatting for this number, so that they all have the same length
			parts = str(val).split(".")
			#Decimal sign
			if len(parts) > 1:
				decdigits = len(parts[1])
				formatstring = '{:0'+str(digits)+'.'+str(decdigits)+'f}'
			#Pad with zeroes if there is only one space left open, as it can't be a decimal
			else:
				formatstring = '{:0'+str(digits)+'d}'
			#Print value
			layerString += formatstring.format(val)
		print layerString
			
		#Print branches
		indent -= numindent

		branchString = " " * indent
		for i, val in enumerate(layerarray):
			freespace = spacing - 2 - digits
			segments = int(floor(freespace / 4))
			if i != 0:
				#Interval of blank space between nodes
				branchString += " " * (spacing-(2-branchfactor(digits)))
			if 2*(offset+i) + 1 < len(tree):
				branchString += "/"
			else:
				break
			if 2*(offset+i) + 2 < len(tree):
				#Interval of blank space between branches for same node
				branchString += " " * (branchspace-2)
				branchString += "\\"
			else:
				break
		print branchString
		
		#Move to the next layer
		offset += 2**currentlayer
		currentlayer += 1
		spacing = (spacing-digits)/2
		
def findIndent(layers, currentlayer, digits, branchspace, numindent):
	if(currentlayer < layers-1):
		return (2**(layers-currentlayer-2)) * (digits + branchspace) - numindent - 1
	return digits-1
			

printBinaryTree([1, 2, 1, 3, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4])