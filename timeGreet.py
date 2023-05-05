import time

timerecruit = time.strftime('%H')
timestamp = int(time.strftime('%H'))
# timestamp = int(input("Please enter: "))

print(type(timestamp))
print(timestamp)

if (timestamp >= 0 and timestamp < 12):
    print("Good morning,sir!")
elif (timestamp >= 12 and timestamp < 17):
    print("Good evening,sir!")
else:
    print("Good night,sir!")
