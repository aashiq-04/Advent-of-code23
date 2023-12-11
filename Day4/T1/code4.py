with open("inp.txt", "r") as file:
    Data=file.read()


import math

def get_points_for_game(winning_number,chosen):
    ans = 0


    for w in winning_number:
        found = False
        pt = -1
        wr = int(w)

        for idx, c in enumerate(chosen):
            cr = int(c)
            if wr == cr:
                found = True
                pt = idx
                break

        if found:
            ans += 1
            chosen[pt] = "-1"

    if ans == 0:
        return 0
    else:
        return int(math.pow(2, ans - 1))

Card_data=Data.strip().split('\n')
sum=0
for i in Card_data:
    card_part=i.split('|')
    win_number=card_part[0].lstrip(':')
    win_number_split=win_number[9:].strip().split(' ')
    chosen_number=card_part[1].strip().split(' ')
    winning_number=[item for item in win_number_split if item]
    chosen=[item for item in chosen_number if item]
    points=get_points_for_game(winning_number,chosen)
    # print(points)
    sum+=int(points)
print(sum)
