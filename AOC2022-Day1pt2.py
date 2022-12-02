#Day 1 part 2

file_object = open(r'C:\Users\whitelawk\Desktop\KJW\Advent 2022\day1input.txt')

calorie_list = file_object.read().splitlines()

calories = 0
max_calories = 0
max_2nd = 0
max_3rd = 0
max_elf = 0

elf_number = 1

for food_item in calorie_list:
    if food_item != '':
        calories += int(food_item)
    else:
        #print (calories)
        if calories > max_calories:
                max_3rd = max_2nd
                max_2nd = max_calories
                max_calories = calories
                max_elf = elf_number
                
        calories = 0
        elf_number += 1
        
#day 1 answer is the number of calories carried by the elf with the most.
print (max_calories+max_2nd+max_3rd)
#print (max_elf)