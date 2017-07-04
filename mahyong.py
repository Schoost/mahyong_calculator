#Mahyong calculator in python
#Author: Joost Kranenborg

players = [1, 2, 3, 4]
totalScores = [0, 0, 0, 0]

#Initializing game
newGame = input("Is this a new game? (Y/n)")
if (newGame == 'n'):
	for player in players:
		totalScores[player-1] = input("Please enter the score for player " + str(player) + ".")

redPlayer = int(input("Please enter the player that has the red bar."))

#Main loop
while True:

	#Print current scores
	print("Current scores:")
	for player in players:
		print("Player " + str(player) + ": " + str(totalScores[player-1]))

	mahyongPlayer = int(input("Please enter the player that is Mahyong."))

	#TODO add confirmation step afterwards
	#Entering the new scores
	roundScores = [0, 0, 0, 0]
	for player in players:
		print("Please enter player " + str(player) + "'s score. Or 'Q' to quit")
		roundScore = int(input())
		if roundScore == "Q":
			exit()
		roundScores[player-1] = roundScore


	#Loop for calculating new scores
	for p1 in players:
		for p2 in players:
			if p1 != p2:
				if (mahyongPlayer != p1 and mahyongPlayer != p2):
					scoreDiff = roundScores[p1-1] - roundScores[p2-1]
				else:
					#mahyong players never pay
					if (mahyongPlayer == p1):
						scoreDiff = roundScores[p1-1]
					else:
						scoreDiff = -roundScores[p2-1]
				
				#Transactions involving red player are doubled
				if (redPlayer == p1 or redPlayer == p2):
					scoreDiff = scoreDiff * 2
				totalScores[p1-1] = totalScores[p1-1] + scoreDiff


	#Increase red player, make sure to wrap 4 to 0
	redPlayer = redPlayer + 1
	if redPlayer > 3:
		redPlayer = 0
