#Day 2 part 1

file_object = open(r'C:\Users\whitelawk\Desktop\KJW\Advent 2022\day2input.txt')

match = file_object.read().splitlines()
 
score = 0

for play in match:
    score += play.count('X')*1 + play.count('Y')*2 + play.count('Z')*3
    win = 0
    if (play.count('X') == 1 and play.count('A') == 1) or (play.count('Y') == 1 and play.count('B') == 1) or (play.count('Z') == 1 and play.count('C') == 1):
        #draw
        win = 3
    if (play.count('A') == 1 and play.count('Y') == 1) or (play.count('B') == 1 and play.count('Z') == 1) or (play.count('C') == 1 and play.count('X') == 1):
        #win
        win = 6
    score += win
    
        
print(score)    