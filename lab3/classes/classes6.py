


#l = list(filter(lambda x :  all(x % i !=0 for i in range(2,int(x/2)+1)),arr))

list = []
n = int(input())
for i in range(n):  
    new_element = int(input())  
    list.append(new_element) 


for i in range(n):
    list = filter(lambda x: x == i or x % i, list)
print(list)

