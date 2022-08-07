from re import A


# input values of skin prices which are int
# if they aren't int values then loop back and ask for the right values
# else store the value
# if the person is done with the calculation then exit the loop
# print the output of the usd value from the skins

# Python program to take integer input  in Python

while True:
    try:
        # input size of the list
        n = int(input("Enter the size of list : "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        # return to the start of the loop
        continue
    else:
        # input was successfully parsed
        break


# store integrs in a list using map, split and strip functions
lst = list(
    map(
        int,
        input("Enter the integer elements of list(Space-Separated): ").strip().split(),
    )
)[:n]
print("The list is:", lst)  # printing the list
