#Run this file through command line without any arguments to play a random episode
#If you want to play a specific episode, run this file with the Season no and the episode no as the command line arguments
#Note that this will only work if you have the episodes of each season in separate directories


import os,sys,random,subprocess
path="E:/Friends/" #Path of your TV Series. F.R.I.E.D.S for example
dir=os.listdir(path)
list=[]
for file in dir:
	list.append(file)
length=len(sys.argv)
if(length>1):
	season=int(sys.argv[1])
	episode_no=int(sys.argv[2])
else:
	season=0
	episode_no=0	
if(season):
	kekrandom=list[season]
else:
	kekrandom=random.choice(list)
path=path+kekrandom
episode=os.listdir(path)
list_episodes=[]
for ep in episode:
	if(ep.endswith(".mkv")): #Give the file extension here. Important!
		list_episodes.append(ep)
if(episode):
	random=list_episodes[episode_no]
else:
	random=random.choice(list_episodes)
#Give the path of your video player here
p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe","\\"+os.path.join(path,random)])
