print("hello, world") 

# Ask user for their name 
name = input("What's your name? ")

#Remove white space from str
name = name.strip()

#Capitalize users name 
name = name.capitalize()

#Capitalize users first and last name
name = name.title()

# Remove white space and capitalize
name = name.strip().title() 

# Ask user for users name, remove white space, and capitalize
name = input("What's your name? ").strip().title()

# Say hello to user
print ("hello,")
print (name)
# another way to say hello
print (f"hello {name}")
# and another way
print ("hello, " +name)
# and another way
print ("hello,", name)




