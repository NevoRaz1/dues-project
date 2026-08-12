from consts import SOLDIER
new_player=[]
for row in range(4):
    new_player.append([])
    for column in range(2):
        new_player[row].append(SOLDIER)
def player_index(row, column):
    index_list=[]
    current_index=[]
    for i in range (row,row+4):
        for j in range (column,column+2):
            index_list.append([i,j])
    return index_list

def foot_index(row, column):
    index_list=[]
    index_list.append([row+3,column])
    index_list.append([row+3,column+1])
    return index_list
