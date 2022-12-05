#Day 4 part 1

file_object = open(r'C:\Users\whitelawk\Desktop\KJW\Advent 2022\day4input.txt')
assignments = file_object.read().splitlines()

counter = 0
elf_1 = 0
elf_2 = 1


for assignment in assignments:
    assignment_list = assignment.split(',')
    print('elf 1 = '+assignment_list[elf_1] +' and elf 2 = '+assignment_list[elf_2])
    elf_1_start = assignment_list[elf_1].split('-')[0] 
    elf_1_end = assignment_list[elf_1].split('-')[1]
    elf_2_start = assignment_list[elf_2].split('-')[0]
    elf_2_end = assignment_list[elf_2].split('-')[1]
    if (elf_1_start <= elf_2_start and elf_1_end >= elf_2_end) or (elf_1_start >= elf_2_start and elf_1_end <= elf_2_end):
        counter += 1
        print ("fully contained, counter = "+str(counter))
        

print(counter)
    
    
    
    