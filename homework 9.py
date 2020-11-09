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
        #global new
        #new = string[:start] + string[start+1:end-1][::-1] + string[end-1:]
        #recursive_string(new)
    #else:
        #ne = ''
        #for i in new:
            #if i != ')':
                #ne+=i
        #print(ne)
#recursive_string("foo(bar(baz))blim")

#Ruben

#exercise 1

#def buildPalindrome(string):
    #st = ''
    #a = string 
    #for i in range(len(string)):
        #if a != a[::-1]:
            #if i>0:
                #a = string
            #st = st + string[i]
            #a+=st[::-1]
    #return a           
#a = "abcd"
#print(buildPalindrome(a))
            
            