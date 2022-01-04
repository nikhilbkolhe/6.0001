# Find cube root of an integer such that it returns the integer closest to the cube root

# Guess and Check Algorithms:
# Start with a guess
# Check if the guess satisfies the condition
# else make another guess

x = int(input("Enter a number: "))

for i in range(x+1):
    if (i**3 >= x):                     # >= because consider x = 9, the 0=>0, 1=>1, 2=>8, 3=>27 -- over here it will go in infinite loop if it is just ==
        break

# not a perfect cube
if (i**3 != x):
    print("Not a perfect cube.")

# cube root of negative number
else:
    if (i < 0):
        i = -i
    print("Cube root of",x,"is :", i)



