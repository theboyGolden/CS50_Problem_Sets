"""
Einstein
Even if you haven’t studied physics (recently or ever!), you might have heard that E = mc^2, wherein
 E represents energy (measured in Joules),
 m represents mass (measured in kilograms), and
 c represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al.
Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
"""


def kilograms_to_joules():
    integer = int(input("Input the number in kg that you'll like to convert to joules\n"))
    speed_of_light = 300000000
    energy = integer * speed_of_light**2
    print(f"the equivalence of {integer}kg in joules is {energy} m/s")


if __name__ == "__main__":
    kilograms_to_joules()
