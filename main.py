import random
import math
from perlin_noise import PerlinNoise
import replit

print("Game Thing py Prkrr20\n\n")
print("1. Perlin Generated")
print("2. Superflat")
menu = input()
ground = []
if (menu == "1"):
	noise = PerlinNoise(octaves=3, seed=random.randint(0, 999999999))

	width = 75
	pic = [noise(i/width) for i in range(width)]
	lowest = min(pic)
	print(lowest)
	pic1 = [math.ceil((noise(i/width)+(abs(lowest)))*10) for i in range(width)]

	g10 = ""
	g9 = ""
	g8 = ""
	g7 = ""
	g6 = ""
	g5 = ""
	g4 = ""
	g3 = ""
	g2 = ""
	g1 = ""


	for i in pic1:
		if (i == 0):
			g1 += "B"
			g2 += " "
			g3 += " "
			g4 += " "
			g5 += " "
			g6 += " "
			g7 += " "
			g8 += " "
			g9 += " "
			g10 += " "
		elif (i == 1):
			g1 += "B"
			g2 += "#"
			g3 += " "
			g4 += " "
			g5 += " "
			g6 += " "
			g7 += " "
			g8 += " "
			g9 += " "
			g10 += " "
		elif (i == 2):
			g1 += "B"
			g2 += "#"
			g3 += "#"
			g4 += " "
			g5 += " "
			g6 += " "
			g7 += " "
			g8 += " "
			g9 += " "
			g10 += " "
		elif (i == 3):
			g1 += "B"
			g2 += "#"
			g3 += "#"
			g4 += "#"
			g5 += " "
			g6 += " "
			g7 += " "
			g8 += " "
			g9 += " "
			g10 += " "
		elif (i == 4):
			g1 += "B"
			g2 += "#"
			g3 += "#"
			g4 += "#"
			g5 += "#"
			g6 += " "
			g7 += " "
			g8 += " "
			g9 += " "
			g10 += " "
		elif (i == 5):
			g1 += "B"
			g2 += "#"
			g3 += "#"
			g4 += "#"
			g5 += "#"
			g6 += "#"
			g7 += " "
			g8 += " "
			g9 += " "
			g10 += " "
		elif (i == 6):
			g1 += "B"
			g2 += "#"
			g3 += "#"
			g4 += "#"
			g5 += "#"
			g6 += "#"
			g7 += "#"
			g8 += " "
			g9 += " "
			g10 += " "
		elif (i == 7):
			g1 += "B"
			g2 += "#"
			g3 += "#"
			g4 += "#"
			g5 += "#"
			g6 += "#"
			g7 += "#"
			g8 += "#"
			g9 += " "
			g10 += " "
		elif (i == 8):
			g1 += "B"
			g2 += "#"
			g3 += "#"
			g4 += "#"
			g5 += "#"
			g6 += "#"
			g7 += "#"
			g8 += "#"
			g9 += "#"
			g10 += " "
		elif (i == 9):
			g1 += "B"
			g2 += "#"
			g3 += "#"
			g4 += "#"
			g5 += "#"
			g6 += "#"
			g7 += "#"
			g8 += "#"
			g9 += "#"
			g10 += "#"

	ground = [g10,g9,g8,g7,g6,g5,g4,g3,g2,g1]
elif (menu == "2"):
	g1 = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
	g2 = "###########################################################################"
	g3 = "###########################################################################"
	g4 = "                                                                           "
	g5 = "                                                                           "
	g6 = "                                                                           "
	g7 = "                                                                           "
	g8 = "                                                                           "
	g9 = "                                                                           "
	g10 = "                                                                           "
	ground = [g10,g9,g8,g7,g6,g5,g4,g3,g2,g1]
else:
	print("something went wrong. please try again later")

py = 0
px = 0
pdir = 1
for i in range(len(ground)):
	if (ground[i][0]=="#"):
		py = i-1
		px = 0
		ground[py] = ground[py][:0] + "o" + ground[py][1:]
		break

#plt.show()
#input()
#plt.close()

Game = True

def mine(dr):
	if (ground[py][px+dr]=="#"):
		ground[py] = ground[py][:px+dr] + " " + ground[py][px+dr+1:]
	elif (ground[py][px+dr]==" "):
		if (ground[py+1][px+dr]=="#"):
			ground[py+1] = ground[py+1][:px+dr] + " " + ground[py+1][px+dr+1:]

def place(dr):
	if (ground[py][px+dr]==" "):
		if (ground[py+1][px+dr]==" "):
			ground[py+1] = ground[py+1][:px+dr] + "#" + ground[py+1][px+dr+1:]
		else:
			ground[py] = ground[py][:px+dr] + "#" + ground[py][px+dr+1:]
	


def move(dr):
	global px
	global py
	global pdir
	pdir = dr
	if not (px == 0 and dr == -1):
		if not (px == 74 and dr == 1):
			if (ground[py][px+dr]==" "):
				ground[py] = ground[py][:px+dr] + "o" + ground[py][px+dr+1:]
				ground[py] = ground[py][:px] + " " + ground[py][px+1:]
				px+=dr
				flyCheck = True
				while flyCheck:
					if (ground[py+1][px]!=" "):
						flyCheck = False
						break
					ground[py+1] = ground[py+1][:px] + "o" + ground[py+1][px+1:]
					ground[py] = ground[py][:px] + " " + ground[py][px+1:]
					py+=1
			elif (ground[py-1][px+dr]==" "):
				ground[py-1] = ground[py-1][:px+dr] + "o" + ground[py-1][px+dr+1:]
				ground[py] = ground[py][:px] + " " + ground[py][px+1:]
				py-=1
				px+=dr


def reg(cmd):
	global Game
	global pdir
	global px
	global py
	if (cmd == "exit()"):
		Game = False
	elif (cmd == "d"):
		pdir = 1
		move(1)
	elif (cmd == "a"):
		pdir = -1
		move(-1)
	elif (cmd == "x"):
		mine(pdir)
	elif (cmd == "p"):
		place(pdir)




while Game:
	replit.clear()
	for i in ground:
		print(i)
	inp = input()
	reg(inp)

print("):")



