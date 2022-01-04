# Approximate Search (Linear Search) algorithm:
# Somewhat similar to Guess and Check
# Start with a guess
# increment guess by small amount and check again
# keep doing this until you reach a good enough solution

x = int(input("Enter the number: "))

guess = 0
epsilon = 0.001
delta = 0.0001
num_of_attempts = 0

while ((abs(guess**3 - x) >= epsilon) and (guess**3 <= x)): # to stop infintite loop
#while (abs(guess**3 - x) >= epsilon): # will loop infinitely for x = 10000
    guess += delta
    num_of_attempts += 1
print("Cube root is:",guess)


