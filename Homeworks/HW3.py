def prime_first(x):
    print(x)

def prime_second(y):
    print(y)

for i in range(0,1000):
    isTrue=True
    if i > 1:
         for k in range(2, i):
            if (i % k) == 0:
                isTrue = False
                break
         if isTrue == True:
             if(i<500):
                 prime_first(i)

             else :
                 prime_second(i)









