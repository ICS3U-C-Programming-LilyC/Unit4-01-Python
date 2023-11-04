#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Nov/3/2023
# This program tells the user the sum of the number they input using a while loop.


def main():
    # Initializing the sum and counter for the loop.
    counter = 0
    sum = 0

    # Telling the user what my program does.
    print("This program will calculate the sum of the number that you enter.")

    # Getting user input.
    user_number_as_string = input("Enter a positive number: ")

    # Initiating Try Catch.
    try:
        user_number_as_integer = int(user_number_as_string)

        # If statement for negative number input.
        if user_number_as_integer <= 0:
            print("Please enter a positive number.")

        # Else statement for valid input.
        else:
            while counter <= user_number_as_integer:
                # Calculating the sum of the user's number.
                sum = sum + counter
                print("Tracking {0} times through loop.".format(counter))

                # Incrementing the counter each time.
                counter = counter + 1

                # Displaying the sum of the user's number back to them.
            print(
                "The sum of your number {} is {}.".format(user_number_as_integer, sum)
            )

    # Catching any errors or invalid inputs.
    except:
        print("Invalid input.")


if __name__ == "__main__":
    main()
