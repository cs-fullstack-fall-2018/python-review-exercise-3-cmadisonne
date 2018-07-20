# Create a loop that quits with q

blackpplmeet = input("Are you single? Press q to quit")

while blackpplmeet != 'q':
    if blackpplmeet == "yes":
        print("Not for long... don't worry")
        print("continue")
    elif blackpplmeet == "no":
        print("You shouldn't be here.")

    blackpplmeet = input("Press q to quit")
