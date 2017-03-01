#!/bin/python3

import sys

# Loop through numbers
# Store a count 
def lonely_integer(a):
    result = 0
    for i in a:        
        print('%s vs %s = %s' % (i, result, result ^ i))
        result = result ^ i
    return result


n = 7 # int(input().strip())
a = [0, 1, 0, 1, 3, 3, 2] # [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))