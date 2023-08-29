name = input("What's your name? ") 

if name == "Harry":
    print("Gryffindor")
elif name == "Hermoine":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
# simplified 
if name == "Harry" or name == "Hermoine" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
# simplified using keyword "match"

match name: 
    case "Harry":
        print("Gryffindor")
    case "Hermoine":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
# match simplified 
match name: 
    case "Harry"|"Hermoine"|"Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
