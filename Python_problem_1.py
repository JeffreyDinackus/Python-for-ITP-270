# 1. Create a variable for your name, age, degree program

name = "Jeff"

age = 24

degree = "Cloud Computing"



# 2. Take the user input for all the three variables

user_name = input("Enter your name")
user_age = input("Enter your age")
user_degree = input("Enter your degree")




# 3. Multiply your age with 3 and divide it by 2 then store the remainder into another variable called remaining age

remaining_age = age * 3 / 2 


# 4. Print a message that will show your name, remaining age and degree program by using string concatenation. 

#the comma makes the python interpreter be able to handle type conversions. 
print("My name is", name + ". my remaining age is", remaining_age, ". My degree program is", degree + "!")
