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
# is_even refined 
def is_even(n):
    return True if n % 2 == 0 else False
# is_even refined even further 
def is_even(n):
    return n % 2 == 0
# call main function
main()
