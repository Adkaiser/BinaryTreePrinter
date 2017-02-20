from math import log, ceil, floor
from BinaryTreeParser import BinaryTreeParser, EMPTYNODESTRING
import sys

def printBinaryTree(tree, valProp=None, leftProp=None, rightProp=None, file=None):
	#Check for an ouptut file
	if file:
		f = open(file, 'w+')
		sys.stdout = f
			
	#If already an array, print array
	if isinstance(tree, list):
		printArrayTree(tree)
		
	#If object-based, parse tree into array based on properties passed to function
	else:
		treearray = BinaryTreeParser(tree, valProp, leftProp, rightProp).parseTree()
		printArrayTree(treearray)
		
	#Reset print to standard stdout
	if file:
		f.close()
		sys.stdout = sys.__stdout__

def printArrayTree(tree):
	printArrayTreeVersioned(tree, 2)
	
def printArrayTreeVersioned(tree, formattingversion):
	#Find number of layers of tree, which equals log(base2) x
	layers = int(ceil(log(len(tree) + 1, 2)))
	currentlayer = 0
	offset = 0
	#Find the largest number that we'll have to deal with
	numbers = filter(lambda x: x != EMPTYNODESTRING, tree)
	largest = max(map(lambda x: str(x), numbers), key=len)
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
				
			#Check if node is a placeholder, and only print a blankspace if it is.
			if str(val) == EMPTYNODESTRING:
				layerString += " "* digits
			#Otherwise print the number
			else:
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
		#Calculate values needed to balance branches
		if(formattingversion == 1):
			indent -= numindent
			branchdistance = branchspace-2
			spacetonextbranch = spacing-(2-branchfactor(digits))
			spacing = (spacing-digits)/2
		
		else:
			#Updated formatting code
			nextindent = findIndent(layers, currentlayer+1, digits, branchspace, numindent)
			indentdiff = indent-nextindent+digits
			indent = nextindent + (indentdiff / 2)
			#Hack to fix indenting on final row as digits get large
			if(currentlayer == layers-2):
				indent += digits/5
			
			spacing = (spacing-digits)/2
			freespacebetween = spacing - digits - 2
			if freespacebetween > -2:
				segment = int(floor(freespacebetween / 4.0))
				branchdistance = segment * 2 + digits
				spacetonextbranch = (spacing + (int(floor(freespacebetween / 2.0))) + digits*2 + branchfactor(digits)/digits)
				if digits%2 == 0 and spacetonextbranch > spacing + digits*2:
					spacetonextbranch += 1
			else:
				segment = 1
				branchdistance = branchspace-2
				spacetonextbranch = spacing + 2*digits

		#Printing spaces and branch symbols
		branchString = " " * indent
		for i, val in enumerate(layerarray):
			if i != 0:
				#Interval of blank space between nodes
				branchString += " " * (spacetonextbranch)
			if 2*(offset+i) + 1 < len(tree):
				#Don't print branches for placeholder nodes
				if tree[2*(offset+i) + 1] == EMPTYNODESTRING:
					branchString += " "
				else:
					branchString += "/"
			else:
				break
			if 2*(offset+i) + 2 < len(tree):
				#Interval of blank space between branches for same node
				branchString += " " * (branchdistance)
				if tree[2*(offset+i) + 2] == EMPTYNODESTRING:
					branchString += " "
				else:
					branchString += "\\"
			else:
				break
		print branchString
		
		#Move to the next layer
		offset += 2**currentlayer
		currentlayer += 1
		
def findIndent(layers, currentlayer, digits, branchspace, numindent):
	if(currentlayer < layers-1):
		return (2**(layers-currentlayer-2)) * (digits + branchspace) - numindent - 1
	return digits-1