import numpy

with open('day3_input.txt') as f:
    priority_offset_cap = 27
    priority_offset_low = 1
    final_offset_cap = ord('A') - priority_offset_cap
    final_offset_low = ord('a') - priority_offset_low
    common_items = []
    priority_sum = 0
    for line in f:
        first_comp = set(line[0:len(line)//2])
        second_comp = set(line[len(line)//2:len(line)])
        common_items.append((first_comp.intersection(second_comp).pop()))
    for i in range(len(common_items)):
        if ord(common_items[i]) <= ord('Z'):
            priority_sum += (ord(common_items[i]) - final_offset_cap)
        else:
            priority_sum += (ord(common_items[i]) - final_offset_low)
    print(priority_sum)
               
            
