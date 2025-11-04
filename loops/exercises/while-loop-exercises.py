# Define three variables for the LaunchCode shuttle - one for the starting fuel level, 
# another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.

fuel = 0
astronauts = 0
altitude = 0


# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, 
  # integer value greater than 5000 but less than 30000. 

while fuel <= 5000 or fuel > 30000:
    fuel = int(input("Enter the starting fuel level: "))

# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). 
# Validate the entry.
  
while astronauts == 0 or astronauts > 7:
    astronauts = int(input("How many astronauts are onboard?"))  
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. 
# Each iteration, decrease the fuel level by 100 units for each astronaut aboard. 
# Also, increase the altitude by 50 kilometers.

while fuel -100 * astronauts >= 0:
    altitude += 50
    fuel -= 100 * astronauts 



# Exercise #2: Print the result with the phrase, 
# he shuttle gained an altitude of ___ km and has ___ kg of fuel left. 
# Fill in the blanks with the altitude and fuel level values.

if altitude >= 2000: 
  ending = "Orbit achieved!"
else:
  ending = "Failed to reach orbit."

print ("The shuttle gained an altitude of " + str(altitude) + " km and has " + str(fuel) + " kg of fuel left. " + ending)


# If the altitude is 2000 km or higher, add “Orbit achieved!” 
# Otherwise add, “Failed to reach orbit.”

