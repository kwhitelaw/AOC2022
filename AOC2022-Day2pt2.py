#Day 2 part 2

file_object = open(r'C:\Users\whitelawk\Desktop\KJW\Advent 2022\day2input.txt')

match = file_object.read().splitlines()

win = 6
draw = 3
rock = 1
paper = 2
scissor = 3 

score = 0

for play in match:
    if play.count('A') == 1:
        if play.count('Z') == 1:
            score += win + paper
        if play.count('Y') == 1:
            score += draw + rock
        if play.count('X') == 1:
            score += scissor
    if play.count('B') == 1:
        if play.count('Z') == 1:
            score += win + scissor
        if play.count('Y') == 1:
            score += draw + paper
        if play.count('X') == 1:
            score += rock
    if play.count('C') == 1:
        if play.count('Z') == 1:
            score += win + rock
        if play.count('Y') == 1:
            score += draw + scissor
        if play.count('X') == 1:
            score += paper

print(score)