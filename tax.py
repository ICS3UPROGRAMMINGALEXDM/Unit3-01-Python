#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: This program calculates the tax paid on a given subtotal in Nunavut

import constants


def main():
    # this function calculates total from subtotal and tax
    print("You are currently in Nunavut where the GST is 5%")
    # get subtotal from the user
    sub_total = float(input("Enter the subtotal: $"))

    # calulate tax and total
    tax = sub_total * constants.GST
    total = sub_total + tax

    # display results

    print("\nThe GST is ${0:,.2f}, and the total cost is: ${1:,.2f}".format(tax, total))


if __name__ == "__main__":
    main()
