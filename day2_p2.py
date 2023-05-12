import numpy

with open('day2_input.txt') as f:
    scores_list = []
    rock = 1
    paper = 2
    scissors = 3
    loss = 0
    tie = 3
    win = 6
    for line in f:
        round_info = list(line)
        round_score = 0
        match round_info[2]:
            case "X":
                round_score += loss
                match round_info[0]:
                    case "A":
                        round_score += scissors
                    case "B":
                        round_score += rock
                    case "C":
                        round_score += paper
                    case _:
                        print("whoops! something bad happened - loss")
            case "Y":
                round_score += tie
                match round_info[0]:
                    case "A":
                        round_score += rock
                    case "B":
                        round_score += paper
                    case "C":
                        round_score += scissors
                    case _:
                        print("whoops! something bad happened - tie")
            case "Z":
                round_score += win
                match round_info[0]:
                    case "A":
                        round_score += paper
                    case "B":
                        round_score += scissors
                    case "C":
                        round_score += rock
                    case _:
                        print("whoops! something bad happened - win")
            case _:
                print("whoops! something bad happened - round end")

        scores_list.append(round_score)
    print(sum(scores_list))                
