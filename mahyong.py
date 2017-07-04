#Mahyong calculator in python

players = [1, 2, 3, 4]

redPlayer = 1
winningPlayer = 1

totalScores = [0, 0, 0, 0]
newScores = [0, 0, 0, 0]

for player in players:
	print("Please enter player " + str(player) + "'s score.")
	newScore = input()
	newScores[player] = newScore

for score in newScores:
	print("Scores: " + str(score))