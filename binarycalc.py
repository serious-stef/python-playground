"""Binary Calculator"""


def main():

    """ Main function. Where the magic happens... """

    binary = input("Please enter binary: ")
    declist = []

    getbinary(binary, declist)
    calcdecimal(binary, declist)
    repeat()


def getbinary(binary, declist):

    """Get binary number"""

    binrange = list(range(2))
    ilength = len(binary) - 1
    i = 0

    while i <= ilength:
        if int(binary[i]) in binrange:
            declist.append(2 ** (ilength - i) * int(binary[i]))
            i = i + 1
        else:
            print(binary + " is not binary!")
            break

    if len(declist) == len(binary):
        return declist


def calcdecimal(binary, declist):

    """This function calculates the decimal number."""

    decimal = 0
    i = 0

    if len(declist) == len(binary):
        while i < len(declist):
            decimal += declist[i]
            i += 1
        print("Binary: " + binary + "\nDecimal: " + str(decimal))
    else:
        exit()


def repeat():

    """ Asking the user to start over again. """

    repeatit = input("Do you want to enter another binary? (y/n)")

    if repeatit == "y":
        main()
    else:
        exit()


main()
