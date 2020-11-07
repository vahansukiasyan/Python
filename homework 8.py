#Narek

#exercise 1

#def big(a):
    #b = [i for i in a if i<0]
    #b.sort(reverse = True)
    #if len(b)<2:
        #return a[-1]*a[-2]*a[-3]
    #else:
        #if a[-1]*a[-2]*a[-3] >= a[-1]*(b[-1]*b[-2]):
            #return a[-1]*a[-2]*a[-3]
        #else:
            #return a[-1]*(b[-1]*b[-2])
#print(big(sorted([9,5,8,5,20,1,2,-3,-2,0])))

#exercise 2

#def author(name,**rest):
    #d = {}
    #for key,value in rest.items():
        #if value[0] == name:
            #d[key] = value[1]
    #srt_d = sorted((value,key) for (key,value) in d.items())
    #for i in srt_d:
        #print(i[1],i[0])
#author("Karen",auth_1=["Karen",2006],auth_2 = ["Narek",1957],auth_3=["Andrew",1374],auth_4 = ["Karen",1769])

#Ruben

#exercise 1

#def answer_queries(k, *query_counts):
    #m  = 0
    #for i in range(1,len([*query_counts])+1):
        #if [*query_counts][i-1] + m - k  >=0:
            #if i == len([*query_counts]):
                #return int((([*query_counts][-1]+m)/k)+i) 
            #if [*query_counts][i-1]+ m - k > 0:
                #m = [*query_counts][i-1]+ m - k
        #else:
            #return i
#print(answer_queries(1,100))


#exercise 2
    

    
#def non_decreasing_sequence(*numbers):
#    my_list = list(numbers)
#    for i in range(1, len(my_list)):
#        if abs(my_list[i - 1]) >= abs(my_list[i]) and my_list[i - 1] >= 0:
#                my_list[i - 1] = -my_list[i - 1]
#        elif abs(my_list[i - 1]) < abs(my_list[i]) and my_list[i] < 0:
#                my_list[i] = -my_list[i]
#    if my_list == sorted(my_list):
#        return 'Yes',my_list
#    return 'No'
#print(non_decreasing_sequence(7,3,-5,-7,9))
    
