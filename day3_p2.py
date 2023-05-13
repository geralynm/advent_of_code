import numpy

with open('day3_input.txt') as f:
    priority_offset_cap = 27
    priority_offset_low = 1
    final_offset_cap = ord('A') - priority_offset_cap
    final_offset_low = ord('a') - priority_offset_low
    elf_group = []
    elf_group_size = 3
    common_items = []
    priority_sum = 0
    for line in f:
        line = line.strip('\n')
        elf_group.append(set(line))
        if len(elf_group) >= elf_group_size:
            group_badge = elf_group[0]
            for i in range(elf_group_size):
                group_badge = group_badge.intersection(elf_group[i])
            common_items.append(group_badge.pop())
            elf_group.clear()
            group_badge.clear()
    for i in range(len(common_items)):
        if ord(common_items[i]) <= ord('Z'):
            priority_sum += (ord(common_items[i]) - final_offset_cap)
        else:
            priority_sum += (ord(common_items[i]) - final_offset_low)
    print(priority_sum)
               
            
