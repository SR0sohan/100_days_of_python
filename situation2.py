y = input("enter the value of y: ")
print(int(y))

# quiz
nm = "harry"
nalen = len(nm)
print(nalen)
# 5-4 = 1; 5-2 = 3; showcase result 1 from 3 "ar"
print(nm[-4:-2])

# driving age

x = input("enter the value of x: ")
y = int(x)
print(x)
print(type(y))
if (y > 18):
    print("You can drive")
else:
    print("You can not drive")

# Multiplication table

a = int(input("Enter the value: "))
for i in range(10):
    print(a, " X", i + 1, "=", a * (i + 1))

# infinite loop:while

i = 0
while True:
    print(i)
    i = i + 1
    if (i % 100 == 0):
        break