#Ruben

#exercise 1

n = input()
nums = []
d = {}
while n != "End":
    nums.append(n)
    n = input()
for m in nums:
    if m in d:
        continue
    else:
        d[int(m)] = nums.count(m)
print(d)

#exercise 2

text = input()
d = {}
x = 0
for i in text:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for val in d.values():
    if val % 2 == 1:
        x+=1
if len(text) % 2 == 0:
    print(False if x>=1 else True)
if len(text) % 2 == 1:
    print(False if x>=2 else True)
#Narek 

exercise 1
for i in range(100):
    for j in range(100):
        if i ** j == j**i and i!=j!=i**j:
            print(i,j,i**j, )
    

#exercise 2

for row in range(1,5):
    for i in range(1,row+1):
        print(row, end=" ")  
    print(" ")