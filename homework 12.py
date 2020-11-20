#Narek

#exercise 1

#currentNumber = 1
#n = int(input())
#flag = False
#stop = 2
#for i in range(n):
    #for column in range(1, stop):
        #print(currentNumber, end=' ')
        #currentNumber += 1        
        #if currentNumber == n+1:
            #flag = True
            #break
    #if flag:
        #break
    #print("")
    #stop += 1
    
#exercise 2

#def find_num(a):
    #for i in range(len(a)):
        #if i == a[i]:
            #return a[i]
        #elif i < a[i]:
            #return -1
    #return -1
#print(find_num([1,2,3,4,5,8,9,10]))

#Ruben 

# exercise 1

#def newRoadSystem(roadRegister):
    #for i in range(len(roadRegister)):
        #if roadRegister[i].count(True) != list(zip(*roadRegister))[i].count(True):
            #return False
    #return True
#print(newRoadSystem([[False,True,False],
        #[False,False,False],
        #[True,False,False]]))
        
#exercise 2

#def efficientRoadNetwork(n, roads):
    #for i in range(n):
        #for j in range(i + 1, n):
            #first = [list(set(road) - set([i]))[0] for road in roads if i in road]
            #second = [list(set(road) - set([j]))[0] for road in roads if j in road]
            #if len(set(first).intersection(set(second))) == 0 and j not in first:
                #return False
    #return True
#print(efficientRoadNetwork(6, [[3, 0], [0, 4], [5, 0], [2, 1],
          #[1, 4], [2, 3], [5, 2]]))