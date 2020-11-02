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
         ['r',0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,'r',0,0],
         [0,0,0,0,0,0,0,0],
         [0,'q',0,0,0,0,0,0,0],
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
def check_king_in_check():
    if (q_cords[0] == k_cords[0] or q_cords[1] == k_cords[1] or abs(q_cords[0] - k_cords[0]) == abs(q_cords[1] - k_cords[1])) or (r1_cords[0] == k_cords[0] or r1_cords[1] == k_cords[1]) or (r2_cords[0] == k_cords[0] or r2_cords[1] == k_cords[1]):
        for i in range(k_cords[0]-1,k_cords[0]+2):
            for j in range(k_cords[1]-1,k_cords[1]+2):
                print(i,j)
                if 9>i>0 and 9>j>0:
                    print(i,j)
                    if q_cords[0] == i or q_cords[1] == j or abs(q_cords[0] - i) == abs(q_cords[1] - j) or r1_cords[0] == i or r1_cords[1] == j or r2_cords[0] == i or r2_cords[1] == j:
                        continue
                    else:
                        return False
                else:
                    continue
        return True
    else:
        return False
print(check_king_in_check())

#Ruben

#exercise 1



#def possible_turns(cell):
    #a = []
    #board = [
             #['A8','B8','C8','D8','E8','F8','G8','H8'],
             #['A7','B7','C7','D7','E7','F7','G7','H7'],
             #['A6','B6','C6','D6','E6','F6','G6','H6'],
             #['A5','B5','C5','D5','E5','F5','G5','H5'],
             #['A4','B4','C4','D4','E4','F4','G4','H4'],
             #['A3','B3','C3','D3','E3','F3','G3','H3'],
             #['A2','B2','C2','D2','E2','F2','G2','H2'],
             #['A1','B1','C1','D1','E1','F1','G1','H1']   
        #]    
    #for i in range(len(board)):
        #for j in range(len(board[i])):
            #if board[i][j] == cell:
                #if 8>i-2>-1 and 8>j-1>-1:
                    #a.append(board[i-2][j-1])
                #if 8>i-2>-1 and 8>j+1>-1:
                    #a.append(board[i-2][j+1])
                #if 8>i+2>-1 and 8>j-1>-1:
                    #a.append(board[i+2][j-1])  
                #if 8>i+2>-1 and 8>j+1>-1:
                    #a.append(board[i+2][j+1]) 
                #if 8>i-1>-1 and 8>j-2>-1:
                    #a.append(board[i-1][j-2])  
                #if 8>i+1>-1 and 8>j-2>-1:
                    #a.append(board[i+1][j-2])  
                #if 8>i+1>-1 and 8>j+2>-1:
                    #a.append(board[i+1][j+2])  
                #if 8>i-1>-1 and 8>j+2>-1:
                    #a.append(board[i-1][j+2])
    #return a
#print(possible_turns("B1"))
