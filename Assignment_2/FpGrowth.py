import numpy as np
import xml.etree.ElementTree as ET
import operator



class Node:
	def __init__(self, key,value):
		self.key = key
        self.value = value
        self.children = None





def Find_Flist(Database,Threshold):
	dict = {}
	for transaction in Database:
		for element in transaction:
			dict[element] = 0
	for transaction in Database:
		for element in transaction:
			dict[element] = dict[element] + 1

	F_List = []
	for key in list(dict):
		if dict[key] < Threshold:
			dict.pop(key,None)
	#print (dict)
	sorted_F_list = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
	#print (sorted_F_list)
	for tupl in sorted_F_list:
		F_List.append(tupl[0])
	return F_List




#Read the xml file and parse the data into a list of sets with the name Database
tree = ET.parse('dblp50000.xml')
root = tree.getroot()
print (root.tag)
print (root.attrib)
Database = []
for child1 in root:
	newset = []
	for child2 in child1:
		if (child2.tag == "author"):
			newset.append(child2.text)
	Database.append(newset)

F_List = Find_Flist(Database,20)


New_Database = []
for transaction in Database:
	L = []
	for element in F_List:
		if element in transaction:
			L.append(element)
	if len(L) != 0:
		New_Database.append(L)





root = Node(None,0)

for transaction in New_Database:
	current_root = root
	for element in transaction:
		if current_root.children == None:
			current_root.children = [Node(element,1)]
			current_root = current_root.children[0]
		else:
			for child in current_root.children:
				if child.key == element:
					child.value = child.value + 1
					current_root = child
					break
			current_root.children.append(Node(element,1))
			current_root = current_root.children[len(current_root.children)-1]

