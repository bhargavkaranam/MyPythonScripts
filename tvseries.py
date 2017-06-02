#!/usr/bin/python


import os,random,subprocess,re,glob

path = "/home/bhargav/Desktop/Friends/"

seasons = os.listdir(path)

historyFile = "/home/bhargav/Desktop/history.txt"

def writeToFile(season,episode):

	with open(historyFile,"a+") as file:
		file.write("Episode " + episode + "\n")


def showHistory():
	print("You recently watched these episodes\n")
	count = 0
	if os.path.exists(historyFile):
		for line in reversed(open(historyFile,"r+").readlines()):
			count = count + 1
			if count == 10:
				break
			print line.rstrip()



def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def playRandom():
	
	global path,seasons
	season = random.choice(seasons)
	path = path + season + "/"
	episodes = os.listdir(path)
	for file in episodes:

		if file.endswith("mkv") or file.endswith("avi"):
			continue
		else:			
			episodes = [x for x in episodes if x != file]

	episode = random.choice(episodes)

	writeToFile(season,episode)

	subprocess.call(['vlc',path + episode])

def playEpisode():
	showHistory()
	global path,seasons
	season = int(raw_input("Which season?\n"))
	episode = int(raw_input("Episode?\n"))
	seasons.sort(key=natural_keys)
	season = seasons[season - 1]
	path = path + season + "/"
	episodes = os.listdir(path)
	
	for file in episodes:

		if file.endswith("mkv") or file.endswith("avi"):
			continue
		else:
			episodes = [x for x in episodes if x != file]

	
	episodes.sort(key=natural_keys)
	
	episode = episodes[episode - 1]

	writeToFile(season,episode)

	subprocess.call(['vlc',path + episode])	

choice = int(raw_input("1. Random\n2. Choose episode\n"))




if choice == 1:
	playRandom()

elif choice == 2:
	playEpisode()




