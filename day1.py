import numpy

with open('day1_input.txt') as f:
    elves = []
    calories = []
    cal_total = []
    num_top_elves = 3
    most_cals = 0
    for line in f:
        if line == "\n":
            cal_total.append(sum(calories))
            elves.append(calories)
            calories.clear()
        else:
            calories.append(int(line))
    cal_total.sort()
    most_cals = sum(cal_total[-num_top_elves:])
    print(most_cals)
            
    
        
