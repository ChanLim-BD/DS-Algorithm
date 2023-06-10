#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'slotWheels' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY history as parameter.
#

def slotWheels(history):
    # Write your code here
    slot = []
    val = 0
    b = 0
    
    for i in range(len(history)):
        slot.append(list(map(int, history[i])))
    
    for i in range(len(slot[0])):
        for i in slot:
            tmp = i.pop(i.index(max(i)))
            if tmp > b:
                b = tmp
        val += b
        b = 0
    
    
    return val
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    history_count = int(input().strip())

    history = []

    for _ in range(history_count):
        history_item = input()
        history.append(history_item)

    result = slotWheels(history)

    fptr.write(str(result) + '\n')

    fptr.close()
