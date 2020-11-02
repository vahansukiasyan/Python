#Narek

#exercise 1

#a = [6,-1,1,7,1,-1,3]
#b = []
#for i in a:
    #if i != -1:
        #b.append(i)
#x = 0
#for i in range(len(a)):
    #if a[i] != -1:
        #a[i] = sorted(b)[x]
        #x+=1
#print(a)


#Ruben

#exercise 1

#def swap_list_elements(list):
    #even = [elem for elem in list if elem%2==0]
    #odd = [elem for elem in list if elem%2==1]
    #count = 0
    #for i in range(len(list)):
        #if i%2==0:
            #list[i] = even[count]
        #else:
            #list[i] = odd[count]
            #count+=1
    #return list
#print(swap_list_elements([1,4,6,5,7,10]))

#exercise 2

#dict_of_points =  {'A': (0, 0), 'B': (0, 4), 'C': (2, 0), 'D': (2, 4), 'E': (0, -4), 'F': (2, -4)}
#def get_count_of_rectangles(dict_of_points):
    #list1 = list(dict_of_points.keys())
    #list2 = []
    #for i in range(len(list1)):
        #for j in range(i + 1, len(list1)):
            #if dict_of_points[list1[j]][0] == dict_of_points[list1[i]][0]:
                #list2.append((list1[i], list1[j]))
    #for i in range(len(list2)):
        #for j in range(i+1,len(list2)):
            #a,b = dict_of_points[list2[i][0]],dict_of_points[list2[i][1]]
            #c,d = dict_of_points[list2[j][0]],dict_of_points[list2[j][1]]
            #print(a,b,c,d)
            


get_count_of_rectangles(dict_of_points)