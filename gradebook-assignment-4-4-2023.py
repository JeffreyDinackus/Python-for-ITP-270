subjects = ["physics",
"calculus",
"poetry",
"history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

gradebook.append(["computer science", 100])

gradebook.append(["visual arts", 93])

gradebook[5][1] = 98

print(gradebook[5])

gradebook.remove(gradebook[2])

gradebook.append(["poetry", "pass"])

#I entered some dummy values because I don't have this array(it is probably available in the code academy)
last_semester_gradebook = [["Math", 100], ["Public Speaking", 100], ["Linux", 100], ["Networking 101", 100]]

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)