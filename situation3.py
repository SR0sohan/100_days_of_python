
#! This program was to read through a file created on this same directory 

f = open("myfile.txt", 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    
    print(f"Marks of student {i} in Maths is: {m1}")
    print(f"Marks of student {i} in English is: {m2}")
    print(f"Marks of student {i} in science is: {m3}")

    print(line)
    
#todo this program is to write and create a file in this same directory

f = open("myfile2.txt", 'w')
lines = ['line 1\n','line 2\n','line 3\n',]

f.writelines(lines)
f.close()

# todo: map, reduce,filter
#todo: MAP

l = [1,2,3,4,6,4,3]

newl = list(map(lambda x: x*x*x, l))
print(newl)


#todo: FILTER

def filter_fucntion(a):
    return a>4 

newnewl = list(filter(filter_fucntion,l))
print(newnewl)
    
#todo: REDUCE
# ! reduce function is not in build in python. it needs to be import manually.
from functools import reduce

numbers = [1,2,3,4,5,6]

mysum = reduce(lambda x, y:x + y, numbers)
print(mysum)  