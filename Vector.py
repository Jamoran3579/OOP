import math        # Used to find square root


class Vector3D:         # Function to initialise the measurements of the vector
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):     # Returns the vector variables in the form of a string
        return "(" + str(self.x) + ".000000, " + str(self.y) + ".000000, " + str(self.z) + ".000000)"

    def __add__(self, vector2):     # Adds together the separate variables of the vectors and creates a new vector
        x = self.x + vector2.x      # using these measurements
        y = self.y + vector2.y
        z = self.z + vector2.z
        new_vector = Vector3D(x, y, z)
        return new_vector           # Returns the new vector

    def __sub__(self,  vector2):    # Subtracts the separate variables of the vectors and creates a new vector
        x = self.x - vector2.x      # using these measurements
        y = self.y - vector2.y
        z = self.z - vector2.z
        new_vector = Vector3D(x, y, z)

        return new_vector

    def __mul__(self, other):
        if type(other) == int:    # Test if the variable passed to the function is an integer and if so, perform
            x = self.x * other    # integer multiplication on the variables of the vector
            y = self.y * other
            z = self.z * other
            new_vector = Vector3D(x, y, z)   # Create a vector from these new measurements

            return new_vector      # Return this new vector

        else:                      # If it is an object, multiply all the measurements together respectively and add
            x = self.x * other.x   # them up
            y = self.y * other.y
            z = self.z * other.z
            scalar = x + y + z

            return str(scalar) + ".0"    # Return this number

    def magnitude(self):                        # Square all measurements of vector and add them together
        holder = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        magnitude = math.sqrt(holder)           # Using math function sqrt to find the root

        return magnitude                        # Returning this value


# Mass of code to test all of the separate methods defined above

v1 = Vector3D(1, 2, 3)                      # Initialising v1
v2 = Vector3D(5, 5, 5)                      # Initialising v2

print("Printing v1")                        # Printing v1
print("v1 = ", v1)

print("Printing v2")                        # Printing v2
print("v2 = ", v2)

v3 = v1 + v2                                # Adding v1 and v2 and printing result
print("Printing addition")
print("v1 + v2 = ", v3)

v4 = v1 - v2                                # Subtracting v1 and v2 and printing result
print("Printing subtraction")
print("v1 - v2 = ", v4)

print("Printing dot product")               # Performing dot product on v1 and v2 and printing result
v5 = v1 * v2
print("v1 * v2 = ", v5)

print("Printing integer multiplication")    # Performing integer multiplication and printing the result
v6 = v1 * 2
print("v1 * 2.5 = ", v6)

print("v1 magnitude is ", v1.magnitude())   # Finding the magnitude of the vector and printing the result
