n=int(input("enter the number of even numbers needed:"))
eve=''
st=(lambda x:(for i in range(0,x))[(str(i)) if i%2==0 else (",")])(n)