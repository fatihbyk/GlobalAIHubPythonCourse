prime_number_list= []
prime_matrix=[]
index_holder=[]

for i in range(0,100):
    isTrue=True
    if i > 1:
         for k in range(2, i):
            if (i % k) == 0:
                isTrue = False
                break
         if isTrue == True:
             prime_number_list.append(i)

for i in range(0,3):
    row_list = []
    for j in range(0,10) :
        index=int(input("Please enter a number that between 0 and 25 :"))
        if (index>=0)&(index<25):
            if index_holder.__contains__(index):
                print("please enter a different number:")

            else:
                index_holder.append(index)
                row_list.append(prime_number_list[index])
                if(len(row_list)==3):
                    break
        else:
            print("number must be on the interval 0,25")

    prime_matrix.append(row_list)
print(prime_matrix)








