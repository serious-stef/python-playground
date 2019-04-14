# Binary calculator

while True:
    binary = input("Please enter binary: ")
    binrange = list(range(2))
    declist = []
    decimal = 0
    ilength = len(binary)-1
    i = 0
    k = 0

    while i <= ilength:
        if int(binary[i]) in binrange:
            declist.append(2**(ilength-i) * int(binary[i]))
            i = i+1
        else:
            print(binary + " is not binary!")
            break

    if len(declist) == len(binary):
        while k < len(declist):
            decimal += declist[k]
            k += 1
        print("Binary: " + binary + "\nDecimal: " +  str(decimal))
    else:
        continue

    repeat = input("Do you want to enter another binary? (y/n)")
    if repeat == "y":
        continue
    else:
        break