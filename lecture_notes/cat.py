#print meow three times 
print("Meow")
print("Meow")
print("Meow")

#using while loops
i = 3
while i != 0:
    print("Meow")
    i = i - 1
#or 
i = 0 
while i < 3:
    print("Meow")
    i += 1 
# using for loops
for i in [0,1,2]: 
    print("Meow")
# using range 
for i in range(3): 
    print("Meow")
#or use _ to say variable isnt important
for _ in range(3): 
    print("Meow")
# using multiplication operator
print("Meow" * 3)
# ask user how many times cat should meow
while True: 
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break
# or 
while True: 
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")


# defining main function
def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")
meow() 

# or 
def main():
    number = get_number()
    meow(number)

def get_number(): 
    while True: 
        n = int(input("What's n? "))
        if n > 0:
            break
    return n 

def meow(n):
    for _ in range(n):
        print("meow")

meow()



