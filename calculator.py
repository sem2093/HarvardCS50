#Calculator ex 1
x = 1
y = 2 
z = x + y 
print(z) 

#Calculator ex 2
# Ask user for x and y values.
x = input("What's x? ")
y = input("What's y? ")
# Add and convert x and y from string to integer 
z = int(x) + int(y) 
print(z) 

#Calculator ex 3 
x= int(input("What's x? "))
y= int(input("What's y? "))

print(x+y)



#calculator ex 4 
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
