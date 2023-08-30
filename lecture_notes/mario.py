# print 3 hashes 
print("#")
print("#")
print("#")

# using for 
for _ in range(3):
    print("#")

# using functions
# define main function
def main():
    print_column(3)
  
# define print_column function
def print_column(height):
    for _ in range(height): 
        print("#")
# or 
def print_column(height):
    print("#" * height) 
  
# call main function
main() 

#print row 
def main():
    print_row(4)

def print_row(width):
    print("?" * width) 

main()

# create a square

def main():
    print_square(3)

def print_square(size):
  # print each row 
    for i in range(size): 
        # print each brick
        for j in range(size):
            print("#", end="")
    #go to next row 
    print()
        
main()

# or
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()

# create a pyramid 

def main(): 
    height = int(input("height: ")) 
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * (i + 1))

if __name__ == "__main__":
    main()
