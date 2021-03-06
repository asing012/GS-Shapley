#!/usr/bin/env python3

# GS-Shapley Algorithm
# Created by: Akshay Singh and
# Date: 09/20/2017
# Purpose: Take argument from user and that number
#          to create indexes and create pairs using GS Algoritm
# INPUT(S): Number of girls and guys
# OUTPUT(S): Number of girls and guys and the processing time
# EXAMPLES: 100   0.0002324479999999962


import time
import sys
from random import randrange

guyIndex = {}

guyPrefer = {}
girlPrefer = {}

girlIndex = {}

"""
   This function accepts girlIndex and guyIndex keys
   and return the keys that are shuffled using Knuth Shuffle.
"""
def knuth_shuffle(shuffle):
        for i in range(len(shuffle)-1, 0, -1):
                z = randrange(i + 1)
                shuffle[i], shuffle[z] = shuffle[z], shuffle[i]
        return shuffle

"""
   Function accepts a list freeMen,
   #that has all the guys who are not engaged.
"""
def free_Men(fm):
        for man in guyPrefer.keys():
                fm.append(man)

"""
   This is the main macthing function
   that does all the stable matching.
   It accepts FreeMen list, engaged dictionary
   and girlEngaged dictionary

   It returns engaged dictionary that has the
   pairs and it return the process time that is
   used to show the CPU time
"""
	

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
