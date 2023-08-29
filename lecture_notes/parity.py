x = int(input("What's x? "))

if x % 2 == 0 :
    print("Even")
else:
    print("Odd")
    
# using functions 
# define main function
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
# define is_even and return bool
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
# call main function
main()
