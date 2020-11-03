from itertools import permutations

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

#def get_count_of_rectangles(dict_of_points):
    #all_variants = list(permutations(dict_of_points.keys(), 4))
    #correct_variants = []
    #for variant in all_variants:
        #if dict_of_points[variant[0]][0] == dict_of_points[variant[1]][0]  and dict_of_points[variant[1]][1] == dict_of_points[variant[2]][1]  and  dict_of_points[variant[2]][0] == dict_of_points[variant[3]][0]  and dict_of_points[variant[0]][1] == dict_of_points[variant[3]][1]:
            #correct_variants.append(''.join(sorted(list(variant))))
    #return set(correct_variants)     
#print(get_count_of_rectangles({'A': (0, 0), 'B': (0, 4), 'C': (2, 0), 'D': (2, 4), 'E': (0, -4), 'F': (2, -4)}))
