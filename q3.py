white = yellow = red = orange = blue = green = 0
while True :
    clr = input("Enter colour :").upper()
    if clr == "STOP":
        break
    elif clr == " WHITE":
        white+=1
    elif clr == "YELLOW":
        yellow+=1
    elif clr == "RED":
        red+=1
    elif clr == "ORANGE":
        orange+=1
    elif clr == "BLUE":
        blue+=1
    elif clr == "GREEN":
        green+=1
    else:
        print("Invalid")
print(" White: ",white)
print("Yellow: ",yellow)
print("Red: ",red)
print("Orange: ",orange)
print("Blue: ",blue)
print("Green: ",green)