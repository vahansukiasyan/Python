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
            
#a = set()  
#x = 0   
#def all_increasing_sequences(k,n,x,l):   
    #if x == n:
        #a.add(tuple([k for k in l]))
    #else:
        #i = 1 if x == 0 else l[x - 1] + 1
        #x += 1    
        #while i <= k: 
            #l[x - 1] = i
            #all_increasing_sequences(k,n,x,l)
            #i += 1
        #x -= 1  
        
#def all_increasing_sequences_print(n,k): 
    #l = [0] * n
    #all_increasing_sequences(k, n, x, l)
    #return a
        
#print(all_increasing_sequences_print(3,5))