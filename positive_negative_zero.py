#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: November 2019
# This program gets numbers from the user and gives
#  the number of positive, negative, and zeros


def main():
    # This program gets numbers from the user and gives
    #  the number of positive, negative, and zeros
    zeros = 0
    positive_numbers = 0
    negative_numbers = 0

    counter = input("How many numbers would you like to enter: ")
    try:
        counter = int(counter)
    except(Exception):
        print("Wrong input!!!\n")
        return

    if counter > 0:
        for counter in range(1, counter + 1):
            number = input("Please enter a number: ")
            try:
                number = int(number)
            except(Exception):
                print("Wrong input!!!")
                return
            if number == 0:
                zeros += 1
            elif number > 0:
                positive_numbers += 1
            elif number < 0:
                negative_numbers += 1
        print("\npositive numbers:", positive_numbers)
        print("zeros:", zeros)
        print("negative numbers:", negative_numbers)
    else:
        print("\nnumber should be more than 0!")


if __name__ == "__main__":
    main()
