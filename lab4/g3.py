n = int(input())
divBy7 = [i for i in range(0, n) if ((i % 3 == 0) and (i % 4 == 0))]
print(divBy7)

def divChecker(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i, value)

divChecker(n)