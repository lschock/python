# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here...

teachers = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],  'Kenneth Love': ['Python Basics', 'Python Collections']}

#part 1.
#For this first task, create a function named num_teachers that takes a single argument, which will be a dictionary of Treehouse teachers and their #courses.
#The num_teachers function should return an integer for how many teachers are in the dict.
def num_teachers(teachers):
  busy_teacher = 0
  for key in teachers.keys():
    busy_teacher += 1
  return busy_teacher

#part 2
#Create a new function named num_courses that will receive the same dictionary as its only argument.
#The function should return the total number of courses for all of the teachers.
def num_courses(teachers):
    total = 0
    for value in teachers.values():
        # for the number of courses within that value
        for course in value:
            total += 1
    return total

#part 3
#For this step, make another new function named courses that will, again, take the dictionary of teachers and courses.
#courses, though, should return a single list of all of the available courses in the dictionary. No teachers, just course names!
def courses(teachers):
    output = []
    for courses in teachers.values():
        output +=courses
    return output

#part 4
#Create a function named most_courses that takes our good ol' teacher dictionary.
#most_courses should return the name of the teacher with the most courses. You might need to hold onto some sort of max count variable.
def most_courses(dic):
    course_count = 0
    teacher_name = ''

    for teacher, courses in dic.items():
        if len(courses) > course_count:
            teacher_name = teacher
    return teacher_name

#part 5
#In this last challenge, I want you to create a function named stats and it'll take our teacher dictionary as its only argument.
#stats should return a list of lists where the first item in each inner list is the teacher's name and the second item is the number of courses that #teacher has. For example, it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]
def stats(dic):
    table = []
    for key in dic:
        count = len(dic[key])
        table += [[key, count]]
    return table
