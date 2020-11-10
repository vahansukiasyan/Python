#Narek

#exercise 1

#def fake_recursion(my_list):
    #if len(my_list) == 1 and my_list[0] == 1:
        #print(a.index(1))
    #else:
        #if sum(my_list[:len(my_list)//2]) % 2 == 1:
            #fake_recursion(my_list[:len(my_list)//2])
        #elif sum(my_list[:len(my_list)//2]) % 2 == 0:
            #fake_recursion(my_list[len(my_list)//2:])
#a = [2,2,2,1,2,2,2,2]
#fake_recursion(a)

#exerxise 2

#def recursive_string(string):
    #if '(' in string:
        #for i in range(len(string)):
            #if string[i] == '(':
                #start = i     
            #elif string[i] == ')':
                #end = i
                #break
        #global new
        #new = string[:start] + string[start+1:end][::-1] + string[end+1:]
        #recursive_string(new)
    #else:
        #print(new)
#recursive_string("foo(bar(baz))blim")

#Ruben

#exercise 1

#def panidrome(string):
    #empty_string = ''
    #default_string = string 
    #for i in range(len(string)):
        #if default_string != default_string[::-1]:
            #if i>0:
                #default_string = string
            #empty_string = empty_string + string[i]
            #default_string+=empty_string[::-1]
    #return default_string           
#default_string = "abbab"
#print(panidrome(default_string))

#exercise 2

#a = set()  
#index_of = 0   
#def all_increasing_sequences(k,n,index_of,my_list):   
    #global a
    #if index_of == n:
        #a.add(tuple([k for k in my_list]))
    #else:
        #i = 1 if index_of == 0 else my_list[index_of - 1] + 1
        #index_of += 1    
        #while i <= k: 
            #my_list[index_of - 1] = i
            #all_increasing_sequences(k,n,index_of,my_list)
            #i += 1
        #index_of -= 1     
#def print_sequences(n,k): 
    #my_list = [0] * n
    #all_increasing_sequences(k, n, index_of, my_list)
    #return a        
#print(print_sequences(3,5))
