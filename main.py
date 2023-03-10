# Program that takes the area of a room as
# input and outputs:
# Area of the floor
# Amount of paint required to paint the walls.
# Volume of the room.

# First we will take the dimensions, using three input statements.
def take_input(str):
    try:
        dimension = float(input(f"Enter {str}: "))
    except ValueError:
        print("You must enter a number.")
        dimension = take_input(str)
    return dimension
    # I considered validating the dimensions of the room but decided that
    # not doing so may provide more utility from a general perspective as 
    # the program could be used on rooms in models or towers with abnormal 
    # dimensions 
    # This simple method of validation simply attempts to convert the user's
    # input into a float. If a TypeError is thrown it is assumed their input 
    # is not in the correct form
length = take_input("length")
width = take_input("width")
height = take_input("height")
# The dimensions are likely not regular, so we convert inputs to floats to be safe
# We are assuming that the room is of regular proportions
# We are also ignoring design features which might impact the proportions e.g. coving
    
# Function for finding the area of the floor
def floor_area(length, width):
    return (length * width)


# Function for finding the surface area of the room
def surface_area(length, width, height):
    pair1 = 2 * (length * width) # Floor and ceiling S.A.
    pair2 = 2 * (length * height) # Pair of walls
    pair3 = 2 * (width * height) # Other pair of walls
    return (pair1 + pair2 + pair3) # Return the sum of all 6 walls

# Function for finding the volume of the room
def volume(length, width, height):
    return (length * width * height)

# Print the results of the calculations by calling the functions.
print("Area of the floor is", floor_area(length, width), "metres squared")
print("Surface area of the room is", surface_area(length, width, height), "metres squared")
print("Volume of the room is", volume(length, width, height), "metres cubed")




