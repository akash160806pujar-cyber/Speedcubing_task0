face = ["red", "blue", "Red", "white", "RED", "blue", "White", "green", "Green"]
white = yellow = red = orange = blue = green = 0
for clr in face :
    clr = clr.upper()
    if clr == "WHITE":
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
print("W appears ",white," times")
print("Y appears ",yellow," times")
print("R appears ",red," times")
print("O appears ",orange," times")
print("B appears ",blue," times")
print("G appears ",green," times")