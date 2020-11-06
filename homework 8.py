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
    #return (sum(query_counts) // k) + 1
#print(answer_queries(1,5,100))


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