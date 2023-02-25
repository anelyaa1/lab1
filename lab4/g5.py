def countdown(n):
    print('Starting')
    while n > 0:
        yield n
        n -= 1

n = int(input())

for n in countdown(n):
    print(n) 