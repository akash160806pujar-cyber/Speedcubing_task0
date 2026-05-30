colors = ["R", "O", "W", "Y", "B", "G", "RED", "ORANGE", "WHITE", "YELLOW", "BLUE", "GREEN"]
face = ["W", "W", "w", "White", "W", "W", "WHITE", "w", "W"]
b = face[0]
flag = 1

for a in face:
    a = a.upper()
    if a not in colors:
        flag = -1
        break
    if a[0] != b[0]:
        flag = 0
        break
    b = a

if flag == 0:
    print("This face is NOT solved.")
elif flag == 1:
    print("This face is solved!")
else:
    print("Invalid Color given")