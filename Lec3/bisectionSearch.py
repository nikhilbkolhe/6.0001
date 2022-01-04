# Bisection Search.
# Begin with a start and end point in a range.
# bisect the range. Check if the target is < or > than bisection point.
# if target lies on the lower part or higher part of bisection point select the endpoints as start and end points as range.
# continue bisecting until you reach close enough to target

x = int(input("Enter the number: "))

epsilon = 0.001
start = 0
end = x
guess = (start + end) / 2
num_of_guesses = 0

while (abs(guess**3 - x) > epsilon):
    num_of_guesses += 1
    if (guess**3 < x):
        start = guess
    else:
        end = guess
    guess = (start + end) / 2

    print("Ouput is:",guess)


