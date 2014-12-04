import pygame
import random

def selection_sort(list):
 
    # Loop through the entire array
    for curPos in range( len(list) ):
        # Find the position that has the smallest number
        # Start with the current position
        minPos = curPos
 
        # Scan left to right (end of the list)
        for scanPos in range(curPos+1, len(list) ):
 
            # Is this position smallest?
            if list[scanPos] < list[minPos]:
 
                # It is, mark this position as the smallest
                minPos = scanPos
 
        # Swap the two values
        temp = list[minPos]
        list[minPos] = list[curPos]
        list[curPos] = temp

def print_list(list):
    for item in list:
        print("{:3}" % tuple(item)),
    print()
 
# Create a list of random numbers
list = []
for i in range(10):
    list.append(random.randrange(100))
 
# Try out the sort
print_list(list)
selection_sort(list)
print_list(list)
