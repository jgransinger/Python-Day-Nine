## LECTURE MATERIAL
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#keys should be / must be strings
#key format is {KEY:VALUE}

print(programming_dictionary["Bug"])

#edit an item in dictionary
programming_dictionary["Bug"] = "a little insect, generally. "

#adding new entry
programming_dictionary["Loop"] = "An action that is repeated over and over again."
print(programming_dictionary)

empty_dictionary = {}

#wipe/clear existing dictionary
#    programming_dictionary = {}

for thing in programming_dictionary:
    print(thing + ":")
    print(programming_dictionary[thing])
#
# -----------------------

#STUDENT SCORE PROJECT WITHIN UDEMY, ASSIGNING TEXT SCORE BASED ON LOOP THROUGH DICTIONARY KEYS AND VALUES
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = student_scores
score = ""

#assigns text value to score by reading value from student_scores dict
for value in student_scores:
    if student_scores[value] >= 91:
        score = "Outstanding"
        student_grades[value] = score
    elif student_scores[value] >= 81:
        score = "Exceeds Expectations"
        student_grades[value] = score
    elif student_scores[value] >= 71:
        score = "Acceptable"
        student_grades[value] = score
    else:
        score = "Fail"
        student_grades[value] = score
print(student_grades)

