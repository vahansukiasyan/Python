#Narek

#exercise 1

def two_strings(str1,str2):
    d1 = {}
    list_str1 = [i for i in str1]
    for i in list_str1:
        if i in d1:
            d1[i] += 1  
        else:
            d1[i] = list_str1.count(i)
    d2 = {}
    list_str2 = [i for i in str2]
    for i in list_str2:
        if i in d2:
            d2[i] += 1 
        else:
            d2[i] = list_str2.count(i)   
    count=0
    for i in d1.keys():
        for j in d2.keys():
            if j != i and d1[i] != d2[i]:
                return False
    return True
print(two_strings("ajjjbg","ajbbjg"))

#exercise 2

def find_num(matrix,num):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == num:
                return i,j
    return False
print(find_num([[10, 20, 30, 40],
 [15, 25, 35, 45],
 [27, 29, 37, 48],
 [32, 33, 39, 50]],29))
 
#Ruben
 
#exercise 1

def financialCrisis(roadRegister):
    answer = []
    for i in range(len(roadRegister)):
        my_list = []
        for j in range(len(roadRegister)):
            if j != i:
                my_list.append(roadRegister[j][:i] + roadRegister[j][i+1:])
        answer.append(my_list)   
    return answer
print(financialCrisis([[False,True,True,False], 
 [True,False,True,False], 
 [True,True,False,True], 
 [False,False,True,False]]))
 
#exercise 2

def namingRoads(roads):
    my_list=[0]*len(roads)
    for lst in roads:
        my_list[lst[2]]=[lst[0],lst[1]]
    for i in range(len(roads)-1):
        for elem in my_list[i+1]:
            if elem in my_list[i]:
                return False
    return True
print(namingRoads([[0,1,0], 
 [4,1,2], 
 [4,3,4], 
 [2,3,1], 
 [2,0,3]]))