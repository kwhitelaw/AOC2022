#Day 3 part 1 2nd attempt

def priority(alpha):
    #A = chr(65) #a = chr(97)
    #priority (a) = 1
    #priority (A) = 27
    p = 0
    if ord(alpha) >= 65 and ord(alpha) <= 90:
        p = ord(alpha) - 38
    elif ord(alpha) >= 97 and ord(alpha) <= 122:
        p = ord(alpha) - 96
    return int(p)

file_object = open(r'C:\Users\whitelawk\Desktop\KJW\Advent 2022\day3input.txt')
pack_list = file_object.read().splitlines()

pack_len = 0
compartment_1_end = 0
item_priority = 0
total_priority = 0

for pack in pack_list:
    pack_len = int(len(pack))
    compartment_1_end = int(len(pack)/2)
    compartment_1 = pack[:compartment_1_end]
    compartment_2 = pack[compartment_1_end:]
    #print (pack)
    #print (len(pack))
    #print (compartment_1)
    #print (len(compartment_1))
    #print (compartment_2)
    #print (len(compartment_2))
    for item in compartment_1:
        for match in compartment_2:
            if item == match:
                item_priority = priority(item)
    total_priority += item_priority
print (total_priority)