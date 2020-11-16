import pprint 
    
#exercise 1

#def size(i):
    #count = 0
    #while i / 10 >= 1:
        #count+=1
        #i/=10
    #return count + 1
#print(size(3749))

#exercise 2

#def func(lst, num):
    #ret_vals = []
    #ret_vals = [(lst[i], num-lst[i]) for i in range(len(lst)) if num - lst[i] in lst]
    #return list(set(ret_vals))
#print(func([5, 2, 2, 5, 3],8))

#Ruben

#exercise 1

#b = []
#def rotate_image(a):
    #for j in range(len(a)):
        #c = []
        #for i in range(len(a)-1,-1,-1):
            #c.append(a[i][j])
        #b.append(c)
    #pprint.pprint(b)
#rotate_image([[10,9,6,3,7],
   #[6,10,2,9,7],
   #[7,6,3,8,2],
   #[8,9,7,9,9],
   #[6,8,6,8,2]])

#exercise 2

#def digitsProduct(product):
    #nums = []
    #first_product = product
    #my_sum = 1
    #if product == 0:
        #return 10
    #elif product == 1:
        #return 1
    #for i in range(9, 1, -1):
        #while(product%i == 0):
            #nums.append(str(i))
            #product /= i
    #for i in nums:
        #my_sum*=int(i)
    #if my_sum == first_product and int(''.join(nums)) > int(''.join(nums[::-1])):
        #return int(''.join(nums[::-1]))
    #else:
        #return -1
#print(digitsProduct(450))

