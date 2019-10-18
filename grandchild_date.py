# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: October 2019
# This program uses Compound Boolean Expressions to solve a problem


def main():
    # this functions use the compound boolean expression

    # input
    age = int(input("Enter your age: "))
    print("")

    # process & output
    if age >= 25 and age <= 45:
        print("You can date my grandchild!")
    else:
        print("You can't date my grandchild")


if __name__ == "__main__":
    main()
