# WAP  to count the number of student with the 'A' grade in the following tuple.
#   ["c", "D", "A", "A", "B", "B", "A"]


grade = ("c", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))


# Store the above values in the list & sort them from "A" to "D".

grade_list = list(grade)
grade_list.sort()
print(grade_list)