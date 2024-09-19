# 킹
import sys
input = sys.stdin.readline

col_dic = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
r_col_dic = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H"}

pos_dic = {"R":(0, 1), "L":(0, -1), "B":(1, 0), "T":(-1, 0),
           "RT": (-1, 1), "LT":(-1, -1) ,"RB":(1, 1), "LB":(1, -1)}

king, stone, n = input().rstrip().split()

king_pos = [9 - int(king[1]), col_dic[king[0]]]
stone_pos = [9 - int(stone[1]), col_dic[stone[0]]]

for i in range(int(n)):
    next_row, next_col = pos_dic[input().rstrip()]

    next_king_x = king_pos[0] + next_row
    next_king_y = king_pos[1] + next_col
    
    if not (1 <= next_king_x <= 8 and 0 <= next_king_y <= 7):
        continue

    if next_king_x == stone_pos[0] and next_king_y == stone_pos[1]:
        next_stone_x = stone_pos[0] + next_row
        next_stone_y = stone_pos[1] + next_col
    else:
        next_stone_x = stone_pos[0]
        next_stone_y = stone_pos[1]

    if not (1 <= next_stone_x <= 8 and 0 <= next_stone_y <= 7):
        continue

    king_pos[0] = next_king_x
    king_pos[1] = next_king_y

    stone_pos[0] = next_stone_x
    stone_pos[1] = next_stone_y

print(r_col_dic[king_pos[1]]+str(9 - king_pos[0]))
print(r_col_dic[stone_pos[1]]+str(9 - stone_pos[0]))

