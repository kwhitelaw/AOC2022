#Day 3 part 2

def priority(alpha):
    p = 0
    if ord(alpha) >= 65 and ord(alpha) <= 90:
        p = ord(alpha) - 38
    elif ord(alpha) >= 97 and ord(alpha) <= 122:
        p = ord(alpha) - 96
    return int(p)

file_object = open(r'C:\Users\whitelawk\Desktop\KJW\Advent 2022\day3input.txt')
pack_list = file_object.read().splitlines()

pack_1 = 0
pack_2 = 0
pack_3 = 0
counter = 0
badge_priority = 0
badge_total = 0

for pack in pack_list:
    if counter % 3 == 0:
        #print ("loading pack 1")
        pack_1 = pack
        pack_2 = 0
        pack_3 = 0
    elif counter % 3 == 1:
        #print ("loading pack 2")
        pack_2 = pack
        pack_3 = 0
    elif counter % 3 == 2:
        #print ("loading pack 3 and comparing")
        pack_3 = pack
        for item in pack_1:
            if (item in pack_2) and (item in pack_3):
                badge_total += priority(item)
                break
    counter += 1

print (badge_total)