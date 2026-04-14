game = input()
score_A = 0
score_B = 0

for i in range(0, len(game), 2):
    if game[i] == "A":
        score_A += int(game[i+1])
    else:
        score_B += int(game[i+1])
    
    if score_A >= 10 and score_B >= 10:
        if score_A - score_B >= 2:
            print("A")
            break
        elif score_B - score_A >= 2:
            print("B")
            break
    elif score_A >= 11:
        print("A")
        break
    elif score_B >= 11:
        print("B")
        break
