#Narek

#exercise 1

#a = [2,8,5,3,4,6,7]
#minn = b = 0
#c = []
#for j in range(2,max(a)): 
    #for i in a:
        #if i % j != 0:
            #minn+= 1
            #if minn == len(a):
                #b = j
                #c.append(b)
        #else:
            #minn = 0
            #break
#print(min(c) if c else max(a)+1)

#exercise 2

#eq = "x+15-1+2=35"
#counter = 0
#for i in range(len(eq)):
    #counter += 1
    #if eq[i] == "=":
        #break
#until = eq[:counter-1]
#print(until)
#after = [eq[counter:]]
#sec_after = [eq[counter:]]
#x = []
#for j in range(len(until)):
    #if not "x" in until[j]:
        #if until[j] == "+":
            #after.append("-")
        #elif until[j] == "-":
            #after.append("+")
        #else:
            #after.append(until[j])
    #else:
        #while sec_after != after:
            #if after[-1] != "+" or after[-1] != "-":
                #x.append(after[-1])
                #after.pop()
                #break
#x.reverse()
#x = "".join(x)
#r = eval("".join(after))
#if x:
    #print(r / int(x))
#else:
    #print(r)

#Ruben

#exercise 2

#text = input()
#wrd_count = 1
#x, y = 0, 0 + wrd_count
#vowels = {}
#consonants = {}
#while wrd_count < len(text):
    #if text[x] in 'aeyuio':
        #vowels[text[x:y]] = vowels.get(text[x:y], 0) + 1
        #x += 1
        #y += 1
    #elif text[x] not in 'aeyuio':
        #consonants[text[x:y]] = consonants.get(text[x:y], 0) + 1
        #x += 1
        #y += 1
    #if y == len(text) + 1:
        #wrd_count += 1
        #x = 0
        #y = 0 + wrd_count
#print(vowels, consonants, sep='\n')
