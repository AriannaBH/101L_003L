import math
import unittest

def total(l):
    sum = 0
    for g in l:
        sum += g
    return sum

def average(values):
    if len(values) == 0:
        return math.nan
    sum = 0
    for val in values:
        sum = sum + val
    return sum/len(values)

def median(l):
    if len(l) <=0 :
        raise ValueError
    l.sort()
    print(l)
    if len(l) % 2 == 1 :
        index=int(len(l)/2)
        return l[index]
    else:
        index=int(len(l)/2)
        sum = l[index]+l[index-1]
        return sum/2