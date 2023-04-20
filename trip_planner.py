# 1.
# Alright, this is it. We are going to use all of our knowledge of functions to build out TripPlanner V1.0.

# First, like in our previous exercises, we want to make sure to welcome our users to the application.

# Create a function called trip_planner_welcome() that takes one parameter called name. The function should use print() to output a message like this:

def trip_planner_welcome(name):
    print("Welcome to tripplanner v1.0 " + name)


# Welcome to tripplanner v1.0 <Name Here>
# Where <Name Here> represents the parameter variable of name we defined.

# Call trip_planner_welcome(), passing your name as an argument.
trip_planner_welcome("Corey")


# Stuck? Get a hint
# 2.
# Next, we are going to define a function called estimated_time_rounded() that will allow us to calculate a rounded time value based on a decimal for our user’s trip.

def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time


# An example call for this function will look like this:

# estimated_time_rounded(2.5)
# Where 2 represents 2 hours and .5 represents 30 minutes.

my_trip_time = estimated_time_rounded(2.5)

# Define the function estimated_time_rounded() with a single parameter estimated_time. The function should do two things:

# Create a variable called rounded_time that is the result of calling the round() built-in function on the parameter estimated_time.
# Return rounded_time.
# After the function definition, call estimated_time_rounded() with a decimal argument and save the result to a variable called estimate. Since this amount represents a time, be sure to use a positive number.


# Stuck? Get a hint
# 3.
# Next, we are going to generate messages for a user’s planned trip.

# Create a function called destination_setup() that will have four parameters in this exact order:

def desintation_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    print("Your trip starts off in " + origin)
    print("And you are traveling to " + destination)
    print("You will be traveling by " + mode_of_transport)
    print("It will take approximately " + str(estimated_time) + " hours")

# origin
# destination
# estimated_time
# mode_of_transport
# Give the parameter mode_of_transport a default value of "Car". The program will error out if we run it since we have not defined a function body yet. Don’t worry we will do that in the next step.


# Stuck? Get a hint
# 4.
# Next, we are going to write four print() statements in our function. The output on this function call should look like this:

# Your trip starts off in <origin>
# And you are traveling to <destination>
# You will be traveling by <mode_of_transport>
# It will take approximately <estimated_time> hours
# Each of these print() statements use a different parameter from our function destination_setup().

# Note: The estimated_time parameter will come in the form of an integer. Make sure to use str() to convert the parameter in your print statement.

# After the function definition, call destination_setup() with the following arguments:
desintation_setup("New York", "London", 15.5, "Car")
# origin and destination should be string values representing the places you will travel from and to
# Use the estimate you created earlier for estimated_time
# If you will be traveling by a mode other than Car, be sure to overwrite the default value of mode_of_transport

# Stuck? Get a hint
# 5.
# Great job! 👏

# We have successfully finished our first version of the trip builder application. Go ahead and try passing different values into your functions!