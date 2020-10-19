#Narek

#exercise 1

#def count_num(a):
    #x=0
    #for i in range(len(a)-1):
        #if a[i]>=a[i+1]:
            #x = x + ((a[i]-a[i+1])+1)
            #a[i+1] = a[i] + 1
    #return x
#print(count_num([1,1,1]))

#exercise 2

#def ascending_list(a):
    #x=0
    #for i in range(len(a)-1):
        #if a[0]>a[i]:
            #x+=1
    #print(True if x<=1 else False,x)
#ascending_list([1,2,1,2])

#Ruben

#exercise 1

#n = int(input())
#a = [[input(),float(input())] for i in range(n)]
#second = sorted(list(set([elem[1] for elem in a])))[1]
#b = [el[0] for el in a if second == el[1]]
#for elem in sorted(b):
    #print(elem)

#exercise 2

#superString = input()
#subString = input()
#x = 0
#z = 0
#for i in range(len(subString)):
    #for j in range(len(superString)):
        #if subString[i] == superString[j]:
            #if x > j:
                #x = j
            #elif z < j:
                #z = j
            #break
#print(superString[x:z + 1])
