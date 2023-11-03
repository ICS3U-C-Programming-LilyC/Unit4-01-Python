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
    user_number_as_sting = input("Enter a positive number: ")

    # Initiating Try Catch.
    try:
        user_number_as_integer = int(user_number_as_sting)

        # Using if statement to error check for negative numbers.
        if user_number_as_integer <= 0:
            print("Please enter a positive number.")

        else:
            while counter <= user_number_as_integer:
                sum = sum + counter
                print("Tracking {0} times through loop.".format(counter))
                counter = counter + 1

                # Displaying the sum of the user's numbers back to them.
            print(
                "The sum of your number {} is {}.".format(user_number_as_integer, sum)
            )

    except:
        print("Invalid input.")


if __name__ == "__main__":
    main()
