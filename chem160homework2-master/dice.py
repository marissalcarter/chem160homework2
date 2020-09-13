from random import choices
ntrials = 15000
player1wins = 0
totalplayer1 = 0
totalplayer2 = 0
for i in range(ntrials):
    dice1 = choices(range(1, 7), k = 2)
    dice1.sort(reverse=True)
    totalplayer2 = totalplayer2 + dice1[0] + dice1[1]
    if totalplayer2 == totalplayer2:
        continue
print("Player2=", dice1)
for i in range(ntrials):
    dice2 = choices(range(1, 7), k = 3)
    dice2.sort(reverse=True)
    totalplayer1 = totalplayer1 + dice2[0] + dice2[1]
    if totalplayer1 > totalplayer2:
        player1wins = player1wins+1
print("Player1=", dice2)
print("ratio of wins=", player1wins/ntrials)