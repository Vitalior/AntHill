# This is a test program designed to help me with multithreading in python
# It has transformed into an "Ant Simulator" or something
# It simulates, an ant hill... Or something...
#
# At the current state you don't gain or lose any workers or fighters, You just kind of, sit there. And watch......
# My fighters need to kick it up a notch :P
# I could mess with the values to put speed it up to an unbelievable degree!
# It's rather fun doing stuff like that.
# I'll upload more videos on this as I update it :)

import thread, time, os, sys, random
from sys import platform as _platform

numWorkers = 5
numFighters = 10
numFood = 15
fightsWon = 0
fightsLost = 0
totalAnts = numFighters+numWorkers
days = 0
lastOutput = ""

f = open("ActLog.lg", "w")

def collectFood(name, delay):
	global numWorkers
	global numFighters
	global totalAnts
	global days
	global numFood
	while True:
		l = random.randint(1, totalAnts)
		time.sleep(delay)
		numFood += numWorkers+l

def fightStuff(name, delay, prob):
	global numWorkers
	global numFighters
	global totalAnts
	global days
	global fightsWon
	global fightsLost
	global lastOutput
	global numFood
	while True:
		time.sleep(delay)
		x = random.randint(0, 100)
		if x < 50:
			f.write("Fight begin.\n")
			y = random.randint(0, 100)
			if y < prob:
				f.write("Fight won\n")
				lastOutput = "Fight Won"
				numFighters += 1
				fightsWon += 1
				numFood -= numFighters
			else:
				f.write("Fight lost\n")
				lastOutput = "Fight Lost"
				fightsLost += 1
				numFighters -= 1
				numFood -= numFighters
		else:
			pass

def youAllHateMe(name, delay):
	global numWorkers
	global numFighters
	global numFood
	global lastOutput
	while True:
		time.sleep(delay)
		x = random.randint(0, 100)
		if x == 0:
			lastOutput = "Everyone died except for a single good fighter. (You will die very soon...)"
			numWorkers = 0
			numFighters = 1
			numFood = 5
		else:
			pass

def starvation(name, delay):
	global numFood
	global lastOutput
	while True:
		time.sleep(delay)
		s = random.randint(1,100)
		if s <= 10:
#			print("Starvation occurs, food halfed.")
			lastOutput = "Couldn't find enough food. Food Halfed."
			numFood = numFood/2
		else:
			pass

def newDay(name, delay):
	global days
	global numFood
	global totalAnts
	global numWorkers
	while True:

		f = random.randint(1, totalAnts)
		r = random.randint(1, totalAnts)
		if r < r/2:
			pass
		else:
			numWorkers += 1
		time.sleep(delay)
		numFood -= totalAnts+f
		days += 1


# Multi Platrform! YAY
if _platform == "linux" or _platform == "linux2":
	cmd = "clear"
elif _platform == "darwin":
	cmd = "clear"
elif _platform == "win32":
	cmd = "cls"


try:
	thread.start_new_thread(collectFood, ("collectFood",5))
	thread.start_new_thread(fightStuff, ("fightStuff",6,40))
#	thread.start_new_thread(drawScreen, ("drawScreen",1))
	thread.start_new_thread(newDay, ("newDay",15))
	thread.start_new_thread(starvation, ("StarvationTest", 1))
except Exception:
	sys.exit()

while True:
	global numFood
	global numFighters
	if numFighters < 1:
		print("Your hill was overrun and everyone died. Game Over")
		lastOutput = "Your hill was overrun and everyone died. Game Over"
		sys.exit()
	elif numFood <= 1:
		print("You ran out of food and everyone died. Game Over")
		lastOutput = "You ran out of food and everyone died. Game Over"
		sys.exit()
	else:
		while True:
			os.system(cmd)
			print """

			Last Output: %s

			Workers: %s
			Fighters: %s

			Food: %s

			fightsWon: %s
			fightsLost: %s

			Day: %s

			""" % (lastOutput, numWorkers, numFighters, numFood, fightsWon, fightsLost, days)
			time.sleep(1)
