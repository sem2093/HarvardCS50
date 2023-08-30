name = input("What's your name?" )
print(f"hello, {name}")

# input into list 

names = []

for _ in range(3):
    name = input("What's your name?" )
    names.append(name)
  
  # simplified 
  names = []

for _ in range(3):
    names.append(input("What's your name?" ))
  # enable print
names = []

for _ in range(3):
    names.append(input("What's your name?" ))

for name in sorted(names):
    print(f"hello, {name}")
  
# using "open" to open file
name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()

# replace "w" with "a" for append 
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()

# add new line after each name 
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# use keyword "with"
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
  
  # enable file reading 
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line)
  
# remove extra line break with "rstrip"
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
  
# simplified 
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
      
      # allow for sorting of names
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
