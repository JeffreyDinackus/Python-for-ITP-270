# 1. Write a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius.
# It should then return c_temp.

#lol I just did this assignment in Javascript for my other class

def f_to_c(f_temp):
    return (f_temp - 32) * (5/9)

temp = f_to_c(100)
print(temp)
# The equation you should use is:

# Temp (C) = (Temp (F) - 32) * 5/9
# 2. Let’s test your function with a value of 100 Fahrenheit.
# Define a variable f100_in_celsius and set it equal to the value of f_to_c with 100 as an input.

# 3. Write a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit.
# It should then return f_temp.

def c_to_f(c_temp):
    return (c_temp * (5/9)) + 32

temp2 = c_to_f(0)
print(temp2)
# The equation you should use is:

# Temp (F) = Temp (C) * (9/5) + 32
# 4. Let’s test your function with a value of 0 Celsius.
# Define a variable c0_in_fahrenheit and set it equal to the value of c_to_f with 0 as an input.

# Use the Force
# 5. Define a function called get_force that takes in mass and acceleration. It should return mass multiplied by acceleration.
# 6. Test get_force by calling it with the variables train_mass and train_acceleration.
# Save the result to a variable called train_force and print it out.

def get_force(train_mass, train_acceleration):
    train_force = train_acceleration * train_mass
    print("The GE train supplies " + str(train_force) + " Newtons of force.")
    return train_force


train_force = get_force(100, 100)
print(train_force)


def get_energy(mass, c=3*10**8):
    print("A 1kg bomb supplies " + str(mass * c^2) +" Joules., with X replaced by bomb_energy.")
    return mass * c^2

# 7. Print the string “The GE train supplies X Newtons of force.”, with X replaced by train_force.
# 8. Define a function called get_energy that takes in mass and c.
# c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8.

# get_energy should return mass multiplied by c squared.
bomb_energy = get_energy(100)
# 9. Test get_energy by using it on bomb_mass, with the default value of c. Save the result to a variable called bomb_energy.
# 10. Print the string “A 1kg bomb supplies X Joules.”, with X replaced by bomb_energy.
# Do the Work
# 11. Define a final function called get_work that takes in mass, acceleration, and distance.
# Work is defined as force multiplied by distance. First, get the force using get_force, then multiply that by distance. Return the result.


#this problem uses the previous function to get the force. 
def get_work(train_mass, train_acceleration, train_distance):
    train_work = get_force(train_mass, train_acceleration) * train_distance
    print("The GE train does "+ str(train_work) +" Joules of work over "+ str(train_distance) +" meters.")
    

x = get_work(100, 1000, 10000)
# 12. Test get_work by using it on train_mass, train_acceleration, and train_distance. Save the result to a variable called train_work.
# 13. Print the string "The GE train does X Joules of work over Y meters.", with X replaced with train_work and Y replaced with train_distance.