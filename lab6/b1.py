def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  

a = [] 
n = int(input())  
for i in range(n):  
    new_element = int(input())  
    a.append(new_element)  

print(multiply((a)))
