from Clock import *
import time

clock = Clock(2, 10, 15)
print(clock.hour)
print(clock.minute)
print(clock.second)
print(clock)
clock.hour = 0
print(clock)
clock = Clock(2,59,58)
print(clock)
clock.tick()
print(clock)
clock.tick() 
print(clock)
clock.tick()
print(clock)

clock = Clock(0, 59, 58, 0)
print(clock)
clock = Clock(0, 59, 58, 1)
print(clock)
clock = Clock(13, 59, 58, 0)
print(clock)
clock = Clock(13, 59, 58, 1)
print(clock)
clock.type = 0
print(clock)

h = int(input('What is the current hour ==> '))
m = int(input('What is the current minute ==> '))
s = int(input('What is the current second ==> '))
clock = Clock(h, m, s, 1)
while True:
    print(clock)
    clock.tick()
    time.sleep(1)