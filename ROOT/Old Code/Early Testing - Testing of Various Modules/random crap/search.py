file = open("super_villains.txt")

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)

print( "There were",len(name_list),"names in the file" )

'''
i = 0
while i < len(name_list) and name_list[i] != "Morgiana the Shrew":
    i += 1
 
if i < len(name_list):
    print( "The name is at position", i)
else:
    print( "The name was not in the list." )
'''

# Binary search
key = "Morgiana the Shrew"; #what do we want to find
lower_bound = 0 # lowest number
upper_bound = len(name_list)-1 # highest number
found = False #once found set to true
while lower_bound <= upper_bound and not found: #still got elements to check?
    middle_pos = (lower_bound+upper_bound) // 2 #finds mid point as integer (//)
    if name_list[middle_pos] < key: #guess is high increase mid point
        lower_bound = middle_pos + 1 
    elif name_list[middle_pos] > key: #guess is low decrease midpoint
        upper_bound = middle_pos - 1
    else:
        found = True #found the target
 
if found:
    print("The name is at position", middle_pos) #print result
else:
    print("The name was not in the list.")

file.close()
