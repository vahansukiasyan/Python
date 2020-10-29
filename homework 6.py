#Narek 

#exercise 1

#squares = ['A1','B5']
#colors = []
#for i in range(len(squares)):
    #if squares[i][0] in "ACEG" and squares[i][1] in "1357" or squares[i][0] in "BDFH" and squares[i][1] in "2468":
        #colors.append("black")
    #else:
        #colors.append("white")
#print(True if colors[0] == colors[1] else False)
    
#exercise 2

board = [[0,0,0,0,0,0,0,0],
         [0,'r',0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,'r',0,0],
         [0,0,0,0,0,0,0,0],
         [0,'q',0,0,0,0,0,0],
         ['k',0,0,0,0,0,0,0],]

f = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 'k':
            k_cords = i+1,j+1
        elif board[i][j] == 'q':
            q_cords = i+1,j+1
        elif board[i][j] == 'r':
            if f == 0:
                r1_cords = i+1,j+1
                f+=1
            else:
                r2_cords = i+1,j+1
print(k_cords,q_cords,r1_cords,r2_cords,sep = '\n')

def check_king_in_check():
    if q_cords[0] == k_cords[0] or q_cords[1] == k_cords[1] or abs(q_cords[0] - k_cords[0]) == abs(q_cords[1] - k_cords[1]) or r1_cords[0] == k_cords[0] or r1_cords[1] == k_cords[1] or r2_cords[0] == k_cords[0] or r2_cords[1] == k_cords[1]:
        for i in range(k_cords[0]-1,k_cords[0]+2):
            for j in range(k_cords[1]-1,k_cords[1]+2):
                if 9<i>0 and 9<j>0 and q_cords[0] == i or q_cords[1] == j or abs(q_cords[0] - i) == abs(q_cords[1] - j) or r1_cords[0] == i or r1_cords[1] == j or r2_cords[0] == i or r2_cords[1] == j:
                    continue
                else:
                    return False
        return True
print(check_king_in_check())
