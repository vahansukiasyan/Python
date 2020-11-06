#Narek

#exercise 1

#def big(a):
    #return a[-1]*a[-2]*a[-3]
#print(big(sorted([9,5,8,5,20,1,2,-3,-2,-1,0])))

#exercise 2

#def author(auth,auth1):
#    print(auth,auth1)
#author("Vahan",auth1=["Vahan",2006])

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
#print(answer_queries(10,5,6))

#exercise 2
    
#def non_decreasing_sequence(*numbers):
    #my_list = [*numbers]
    #for i in range(len(my_list)):
        #for j in range(len(my_list)):
            #my_list[i] =  -my_list[i]
            #my_list[j] =  -my_list[j]
            #if my_list == sorted(my_list):
                #return 'Yes',my_list
            #else:
                #my_list[i] =  -my_list[i]
                #my_list[j] =  -my_list[j]
    #return 'No'
#print(non_decreasing_sequence(0,4,3))    
