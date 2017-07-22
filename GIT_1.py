import random

for i in range(10):
    print(random.randint())

x = 1
y = 4

while x != y:
    print("Unsuccessful")
    if y > x:
        y += 1
    else:
        y -= 1
        
print ("Successful")
