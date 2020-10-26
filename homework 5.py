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
        
#if t:
    #print(flag,t)
#else:
    #print(flag)

#Ruben

#exercise 1

an = []
xmb = input()
xmb1,xmb2 = xmb.split(", ")
for i in range(len(xmb.split(", "))):
    anun = input().split(",")
    an.append((anun))
    print(an)
stug = input().split(", ")
for i in stug:
    for j in an:
        if i in j:
            print("Something")
#l = []
#for i in range(len(an)):
    #for j in range(len(an) + i):
        #l.append(an[i][j])
#b = []
#for i in l:
    #for j in stug:
        #if j == i:
            #b.append(j)
#for i in range(len(b)-1):
    #if b[i-1] == b[0]:
        #b.remove(b[i])
#x = 0
#y = ""
#if b[0] in an[0]:
    #x = str(len(an[0]))
#elif b in an[1]:
    #x = str(len(an[1]))
#if x in xmb1.split(": "):
    #y = xmb1.split(": ")[0]
#elif x in xmb2.split(": "):
    #y = xmb2.split(":")[0]
#print(b[0],": ",y)

#matem: 3, yandex: 2
#aleqs,petrov
#ivanov,aleqs,sidorov
#ivanov, aleqs

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

