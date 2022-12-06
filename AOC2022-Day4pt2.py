#Day 4 part 2

def between(alpha,bravo,charlie):
    result = bool(0)
    if bravo >= alpha and bravo <= charlie:
        result = bool(1)
    return result

file_object = open(r'C:\Users\whitelawk\Desktop\KJW\Advent 2022\day4input.txt')
assignments = file_object.read().splitlines()

counter = 0
elf_1 = 0
elf_2 = 1


for assignment in assignments:
    assignment_list = assignment.split(',')
    #print('elf 1 = '+assignment_list[elf_1] +' and elf 2 = '+assignment_list[elf_2])
    elf_1_start = int(assignment_list[elf_1].split('-')[0])
    elf_1_end = int(assignment_list[elf_1].split('-')[1])
    elf_2_start = int(assignment_list[elf_2].split('-')[0])
    elf_2_end = int(assignment_list[elf_2].split('-')[1])
    if between(elf_1_start,elf_2_start,elf_1_end) or between(elf_1_start,elf_2_end,elf_1_end) or between(elf_2_start,elf_1_start,elf_2_end) or between(elf_2_start,elf_1_end,elf_2_end):
        counter +=1

print(counter)
    