import numpy as np
import xml.etree.ElementTree as ET






def Generate_Itemset(Itemset,length):
	New_ItemSet = []
	for i in range(0,len(Itemset)):
		for j in range(0,len(Itemset)):
			if j>i:
				New_Set = Itemset[i].union(Itemset[j])
				if len(New_Set) == length:
					New_ItemSet.append(New_Set)
	return New_ItemSet


def Cal_Support(Itemset,Database):
	Dict = {}
	for Item in Itemset:
		Dict[frozenset(Item)] = 0
	for Transaction in Database:
		for Item in Itemset:
			if Item.issubset(Transaction):
				Dict[frozenset(Item)] = Dict[frozenset(Item)] + 1

	return Dict


def Pruning_Candidates(dic_Itemset,Threshhold):
	New_Candidate_List = []
	for key in dic_Itemset:
		if dic_Itemset[key] >= Threshhold:
			New_Candidate_List.append(key)
		
	return New_Candidate_List


"""
#Read the xml file and parse the data into a list of sets with the name Database
tree = ET.parse('dblp50000.xml')
root = tree.getroot()
print (root.tag)
print (root.attrib)
Database = []
for child1 in root:
	newset = set()
	for child2 in child1:
		if (child2.tag == "author"):
			newset.add(child2.text)
	Database.append(newset)

"""



a = {1}
b = {2}
c = {3}
Database = [{1,2,3},{1,2},{2,3},{1,2,3}]
L = [a,b,c]

print (Generate_Itemset(L,2))
print (Cal_Support(Generate_Itemset(L,2),Database))
print (Pruning_Candidates(Cal_Support(Generate_Itemset(L,2),Database),3))








