mark=float(input("Input your numer..."))
index=int(mark/10)

match index:
    case 10|9|8:
        print("A+")
    case 7:
        print("A")
    case 6:
        print("B")
    case _:
        print("F")