#!/usr/bin/env python3
import sys
import subprocess


numberList = [1000,1500,2000,2500,3000,3500,4000,4500,5000]
data = open("data.txt","w")
for i in numberList:
	subprocess.call(["./gs1.py", str(i)], stdout=data)
data.close()


