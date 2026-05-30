colors = ["W", "Y", "R", "O", "B", "G"]
face = [ ["R", "R", "G"], ["R", "W", "G"], ["B", "B", "Y"] ]

for a in face:
    for b in a:
        if b in colors:
            print(b, end = " ")
        else:
            print("(Invalid)", end = " ")
    print(" ")

print(" ")
for a in face:
    for b in a:
        if b in colors:
            if b == "R":
                b = "X"
            print(b, end = " ")
        else:
            print("(Invalid)", end = " ")
    print(" ")