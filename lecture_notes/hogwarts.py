students = ["Harry", "Hermoine", "Ron"]
# print students 
print(students[0])
print(students[1])
print(students[2])

# or 
for student in students:
    print(student)

# or 
for i in range(len(students)):
    print(students[i])
  
# list students using dict 
students = {
    "Hermoine":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin"
}

for student in students: 
    print(student, students[student])

# putting dictionaries in a list

student = [
    {"name": "Hermoine","house":"Gryffindor","patronus": "Otter"},
    {"name": "Harry","house":"Gryffindor","patronus": "Stag"},
    {"name": "Ron","house":"Gryffindor","patronus": "Jack russel terrier"},
    {"name": "Draco","house":"Slytherin","patronus": none }
]

for student in students:
    print(student["name"], student["house"], student["patronus"])
