#Narek

#exercise 1

#def winner(board):
    #if "Empty" in board[0] or "Empty" in board[1] or "Empty" in board[2]:
        #x = []
        #o = []
        #for i in board:
            #for j in i:
                #if j == "x":
                    #x.append(j)
                #elif j == "o":
                    #o.append(j)
        #if len(x) > len(o):
            #return "o"
        #else:
            #return "x"    
    #else:
        #for row in range(0,3):
            #if board[row][0]==board[row][1]==board[row][2]=="x":
                #player = "x is winner"
            #elif board[row][0]==board[row][1]==board[row][2]=="o":
                #player = "o is winner"
        #for col in range(0,3):
            #if board[0][col]==board[1][col]==board[2][col]=="x":
                #player = "x is winner"
            #elif board[0][col]==board[1][col]==board[2][col]=="o":   
                #player = "o is winner"
        #if board[0][0]==board[1][1]==board[2][2]=="x":
            #player = "x is winner"
        #elif board[0][0]==board[1][1]==board[2][2]=="o":
            #player = "o is winner"
        #if board[0][2]==board[1][1]==board[2][0]=="x":
            #player = "x is winner"
        #elif board[0][2]==board[1][1]==board[2][0]=="o":
            #player = "o is winner"
        #if board[0][0]==board[1][1]==board[2][2]=="x":
            #player = "x is winner"
        #elif board[0][0]==board[1][1]==board[2][2]=="o":
            #player = "o is winner"
        #if board[0][2]==board[1][1]==board[2][0]=="x":
            #player = "x is winner"
        #elif board[0][2]==board[1][1]==board[2][0]=="o":
            #player = "x is winner"
        #if player == "":
            #return -1
        #else:
            #return player
#print(winner([["x","o","x"],
            #["o","x","o"],
            #["x","o","o"]]
            #))
            
#exercise 2            

#a = [4,14,24,29]
#t = []

#flag = False
#for x in range(3,int(max(a)-1)):
    #g = []
    #for i in range(1,len(a)):
        #z = a[1] % x
        #if a[i] % x == z:
            #g.append(a[i])
            #if len(a)-1 == len(g):
                #flag = True
                #break
    #if flag:
        #t.append(a[0])
        #t.append(a[1])
        #for h in range(1,max(a)):
            #if t[h] > max(a)-1:
                #break
            #t.append(t[h] + x)
        #break
 
#print(flag,t if t else flag)


#Ruben

#exercise 1

#names = []
#groups = input().split(', ')
#for i in range(len(groups)):
    #anun = input().split(",")
    #names.append((anun))
#stug = input().split(", ")
#d = []
#dic = {}
#b = []
#for i in stug:
    #for j in names:
        #if i in j:
            #d.append(i)
#for i in set(d):
    #dic[i] = d.count(i)
#minval = min(dic.values())
#res = [k for k, v in dic.items() if v==minval]
#for j in names:
    #if i in j:
        #subject = len(j)
#for g in groups:
    #if int(subject) == int(g.split(': ')[1]):
        #sub = g.split(': ')[0]
#for i in sorted(res):
    #print(i + ': ' + sub)
    
    #matemathics: 3, yandex: 2
    #Alex,Mary
    #Garry,Alex,Edgar
    #Garry, Alex

#exercise 2

#d = []
#count = 1
#total = 0
#def add_item(itemName,itemCost):
    #global d,count
    #d.append([itemName,itemCost])
    #return d

#def print_receipt():
    #global count,total,d
    #if len(d) == 0:
        #return
    #print('Check {} Number of items: {}'.format(count,len(d)))
    #for i in range(len(d)):
        #total += d[i][1]
        #print('{} - {}'.format(d[i][0], d[i][1]))
    #count += 1
    #print('Total: ' + str(total))
    #print('-' * 5)
    #total = 0
    #d = []
#add_item("notepad" , 100)
#add_item("book",10)
#print_receipt()
#add_item('pen',150)
#print_receipt()

