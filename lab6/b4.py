from time import sleep
import math
def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)

a = int(input())
b = int(input())
print("Square root after specific miliseconds:") 

print(delay(lambda x: math.sqrt(x), a, b))
