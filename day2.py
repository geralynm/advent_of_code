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
                round_score += rock
                match round_info[0]:
                    case "A":
                        round_score += tie
                    case "B":
                        round_score += loss
                    case "C":
                        round_score += win
                    case _:
                        print("whoops! something bad happened - rock")
            case "Y":
                round_score += paper
                match round_info[0]:
                    case "A":
                        round_score += win
                    case "B":
                        round_score += tie
                    case "C":
                        round_score += loss
                    case _:
                        print("whoops! something bad happened - paper")
            case "Z":
                round_score += scissors
                match round_info[0]:
                    case "A":
                        round_score += loss
                    case "B":
                        round_score += win
                    case "C":
                        round_score += tie
                    case _:
                        print("whoops! something bad happened - scissors")
            case _:
                print("whoops! something bad happened - shape you selected")

        scores_list.append(round_score)
    print(sum(scores_list))                
