#!/usr/bin/env python3
# GS-Shapley Algorithm
# Created by: Akshay Singh and 
# Date: 
# Purpose: 
# INPUT(S)::
# OUTPUT(S):
# EXAMPLES:


import time
import sys
from random import randrange

guyIndex = {}

guyPrefer = {}
girlPrefer = {}

girlIndex = {}

#COPIED-------------------------------
def knuth_shuffle(x):
	for i in range(len(x)-1, 0, -1):
		j = randrange(i + 1)
		x[i], x[j] = x[j], x[i]
	return x
#--------------------------------------


def free_Men(fm):
	for man in guyPrefer.keys():
		fm.append(man)
	

def matching(fm,engaged,girlEngaged):
	t = time.process_time()	
	while(len(fm) > 0):
		for man in guyPrefer.keys():
			
			for woman in guyPrefer[man]:
				#print(guyIndex[man],"proposes to"," ",girlIndex[woman])
				if(woman not in girlEngaged):
					engaged[man] = woman
					girlEngaged[woman] = man
					fm.remove(man)
					#print(guyIndex[man], " engaged to ", girlIndex[woman])
					break
				else:	
					currentGuy = girlEngaged[woman]
					currentGuyIndex = girlPrefer[woman].index(currentGuy)
					newGuyIndex = girlPrefer[woman].index(man)
					
					if(currentGuyIndex > newGuyIndex):

						engaged[man] = woman
						girlEngaged[woman] = man
						fm.remove(man)
						del engaged[currentGuy]
						fm.append(currentGuy)					
						#print(girlIndex[woman]," dumps", guyIndex[currentGuy])
						#print(guyIndex[man], " engaged to ", girlIndex[woman])
						break
													
		break
	
	return engaged,(time.process_time() - t)

def main():
	freeMen = []
	engaged = {}
	girlEngaged = {}
	
	numberOfSuitors = int(sys.argv[1])
	#print(numberOfSuitors)
	#print(type(numberOfSuitors))
	#temp = int(numberOfSuitors / 2)
	#guysLists = list(range(0,temp))
	#girlsLists = list(range(0,temp))
	
	#test = {}

	
	for i in range(0,numberOfSuitors):
			
		guyIndex[i] = i

	for i in range(0,numberOfSuitors):
		girlIndex[i] = i

	#print(guysLists)

	for key, value in guyIndex.items():
		guyPrefer[key] = list(knuth_shuffle(list(girlIndex.keys())))
	for key, value in girlIndex.items():
		girlPrefer[key] = list(knuth_shuffle(list(guyIndex.keys())))
	
	#print("GUY PREFER",guyPrefer)
	#print("GIRL PREFER", girlPrefer)			
	
	free_Men(freeMen)
	engagedValue,processTime = matching(freeMen,engaged,girlEngaged)
	#matching(freeMen,engaged,girlEngaged)
	print(numberOfSuitors," ",processTime)
	#print(numberOfSuitors)
main()
