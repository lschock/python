x = 115
y = 1
z = 112

while (x) > (z):
    x -= y
print(x)




temp = 115
while temp > 112:
    temp -= 1
print(temp)


teachers = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],  'Kenneth Love': ['Python Basics', 'Python Collections']}
def num_teachers(teachers):
    return len(teachers.keys())
    

course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 189, "Java Basics": 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long.".format(course, minutes))
