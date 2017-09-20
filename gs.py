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

guyIndex = {0: "John", 1:"Jack", 2:"Jim", 3:"Kapi", 4:"Rhys", 5:"Oman", 6:"Kirk", 7:"Erik", 8:"Yaz", 9:"Amos"}


guyPrefer = {}

girlPrefer = {}

girlIndex = {0:'Ele', 1:'Ema', 2:'Cath', 3:'Kate', 4:'Sara', 5:"Ivy", 6:"Hope", 7:"Kim", 8:"Sam", 9:"Sahr"}

"""
   This function accepts girlIndex and guyIndex keys
   and return the keys that are shuffled using Knuth Shuffle.
"""
#COPIED-------------------------------
def knuth_shuffle(x):
	for i in range(len(x)-1, 0, -1):
		j = randrange(i + 1)
		x[i], x[j] = x[j], x[i]
	return x
#--------------------------------------

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
	#t1 = time.time()
	while(len(fm) > 0):
		for man in guyPrefer.keys():
			#print(guyIndex[man],"proposes to"," ", end="")
			for woman in guyPrefer[man]:
				print(guyIndex[man],"proposes to"," ",girlIndex[woman])
				if(woman not in girlEngaged):
					engaged[man] = woman
					girlEngaged[woman] = man
					fm.remove(man)
					print(guyIndex[man], " engaged to ", girlIndex[woman])
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
						print(girlIndex[woman]," dumps", guyIndex[currentGuy])
						print(guyIndex[man], " engaged to ", girlIndex[woman])
						break
													
		break
	return engaged,(time.process_time() - t)#, (time.time()-t1)

"""
   This is the main function that calls all the functions
"""
def main():

	freeMen = []
	engaged = {}
	girlEngaged = {}
	
	for key, value in guyIndex.items():
		guyPrefer[key] = list(knuth_shuffle(list(girlIndex.keys())))
	for key, value in girlIndex.items():
		girlPrefer[key] = list(knuth_shuffle(list(guyIndex.keys())))
	
	print("Participants:")
	for key, value in guyPrefer.items():
		print(guyIndex[key]," ", end="")
	print("\n")
	for key, value in girlPrefer.items():
		print(girlIndex[key]," ", end="")
	print("\n")
	
	print("Preferences:")
	for key, value in guyPrefer.items():
		print(guyIndex[key],":", end="")
		for i in value:
                	print(girlIndex[i], ",", end="")
		print("")
       		
	free_Men(freeMen)
	print("\n")
	for key, value in girlPrefer.items():
		print(girlIndex[key],":", end="")
		for i in value:
			print(guyIndex[i], ",", end="")
		print("")
	engaged,timeProcess = matching(freeMen, engaged, girlEngaged)
	
	print("Pairing :")
	for key, value in engaged.items():
		print(" ",guyIndex[key],"-", girlIndex[value])

	#print(engaged)
#	print("Elapsed wall clock time: ", timeClock)
	print("Elapsed CPU time: ", timeProcess)
	print("Stable matchup") 

	#Taking User Input
	person = input('Another trial? (y)es, (n)o ')
	while(person == 'y' or 'yes'):
		#person = input("Another trial? (yes), (n)o")
		main()
			
main()
