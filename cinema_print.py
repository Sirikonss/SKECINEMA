def translator_100(n):
    if n == "J" :
        n = 0
    elif n == "I" :
        n = 1
    elif n == "H" :
        n = 2
    elif n == "G" :
        n = 3
    elif n == "F" :
        n = 4
    elif n == "E" :
        n = 5
    elif n == "D" :
        n = 0
    elif n == "C" :
        n = 1
    elif n == "B" :
        n = 2
    elif n == "A" :
        n = 3
    return  n

def seat_100(row_n,col_n,row_h,col_h) :
    normal_Seat = []
    honeymoon_Seat = []
    normal = ["J", "I", "H", "G", "F", "E", "D"]
    honeymoon = ["C", "B", "A"]
    column = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(len(normal)):
        normal_Seat.append([])
        for j in range(len(column)):
            normal_Seat[i].append(f"{normal[i]}{column[j]}")
    for k in range(len(honeymoon)):
        honeymoon_Seat.append([])
        for l in range(len(column)):
            honeymoon_Seat[k].append(f"{normal[k]}{column[l]}")

    for a in range(len(row_n)):
        normal_Seat[row_n[a]][col_n[a]] = "X"

    for b in range(len(row_h)):
        honeymoon_Seat[row_h[b]][col_h[b]] = "X"

    return normal_Seat,honeymoon_Seat

def seat_120(row_n,col_n,row_h,col_h) :
    normal_Seat = []
    honeymoon_Seat = []
    normal = ["J","I","H","G","F","E"]
    honeymoon = ["D","C","B","A"]
    column = [1,2,3,4,5,6,7,8,9,10,11,12]
    for i in range(len(normal)):
        normal_Seat.append([])
        for j in range(len(column)):
            normal_Seat[i].append(f"{normal[i]}{column[j]}")
    for k in range(len(honeymoon)):
        honeymoon_Seat.append([])
        for l in range(len(column)):
            honeymoon_Seat[k].append(f"{normal[k]}{column[l]}")

    for a in range(len(row_n)):
        normal_Seat[row_n[a]][col_n[a]] = "X"

    for b in range(len(row_h)):
        honeymoon_Seat[row_h[b]][col_h[b]] = "X"

    return normal_Seat,honeymoon_Seat

def seat_150(row_n,col_n,row_h,col_h) :
    normal_Seat = []
    honeymoon_Seat = []
    normal = ["J", "I", "H", "G", "F", "E"]
    honeymoon = ["D", "C", "B", "A"]
    column = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for i in range(len(normal)):
        normal_Seat.append([])
        for j in range(len(column)):
            normal_Seat[i].append(f"{normal[i]}{column[j]}")
    for k in range(len(honeymoon)):
        honeymoon_Seat.append([])
        for l in range(len(column)):
            honeymoon_Seat[k].append(f"{normal[k]}{column[l]}")

    for a in range(len(row_n)):
        normal_Seat[row_n[a]][col_n[a]] = "X"

    for b in range(len(row_h)):
        honeymoon_Seat[row_h[b]][col_h[b]] = "X"

    return normal_Seat, honeymoon_Seat

def print_cinema_100(normal_Seat,honeymoon_Seat) :
    normal = ["J", "I", "H", "G", "F", "E", "D"]
    honeymoon = ["C", "B", "A"]
    column = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print()
    # print("--------------------------------------------------------------")
    print("|\x1b[0;30;47m                          Screen                            \x1b[0m|")
    # print("--------------------------------------------------------------")
    print()
    print()
    for i in range(len(normal_Seat)):
        print("    "+normal[i] + " ", end="")
        for j in range(len(normal_Seat[i])):
            if normal_Seat[i][j] == "X":
                print(f"|\x1b[0;37;47m    \x1b[0m", end="")
            else:
                print(f"|\x1b[0;31;41m    \x1b[0m", end="")
        print()
        print("       -------------------------------------------------")


    print()
    for q in range(len(honeymoon_Seat)):
        print("    "+honeymoon[q] + " ", end="")
        for r in range(len(honeymoon_Seat[q])):
            if honeymoon_Seat[q][r] == "X":
                print(f"|\x1b[0;37;47m    \x1b[0m", end="")
            else:
                print(f"|\x1b[0;35;45m    \x1b[0m", end="")
        print()
        print("       -------------------------------------------------")

    print("         1    2    3    4    5    6    7    8    9   10")
    print()
    print("               \x1b[0;31;41m    \x1b[0m  220 Baht      \x1b[0;35;45m    \x1b[0m  240 Baht")

    return ""

def print_cinema_120(normal_Seat,honeymoon_Seat) :
    normal = ["J", "I", "H", "G", "F", "E"]
    honeymoon = ["D", "C", "B", "A"]
    print()
    # print("--------------------------------------------------------------")
    print("|\x1b[0;30;47m                          Screen                              \x1b[0m|")
    # print("--------------------------------------------------------------")
    print()
    print()
    for i in range(len(normal_Seat)):
        print(normal[i] + " ", end="")
        for j in range(len(normal_Seat[i])):
            if normal_Seat[i][j] == "X":
                print(f"|\x1b[0;37;47m    \x1b[0m", end="")
            else:
                print(f"|\x1b[0;31;41m    \x1b[0m", end="")
        print()
        print()
    print()
    for q in range(len(honeymoon_Seat)):
        print(honeymoon[q] + " ", end="")
        for r in range(len(honeymoon_Seat[q])):
            if honeymoon_Seat[q][r] == "X":
                print(f"|\x1b[0;37;47m    \x1b[0m", end="")
            else:
                print(f"|\x1b[0;35;45m    \x1b[0m", end="")
        print()
        print()
    print("     1    2    3    4    5    6    7    8    9   10   11   12")
    print()
    print("               \x1b[0;31;41m    \x1b[0m  220 Baht      \x1b[0;35;45m    \x1b[0m  240 Baht")

    return ""

def print_cinema_150(normal_Seat,honeymoon_Seat) :
    normal = [ "J", "I", "H", "G", "F", "E"]
    honeymoon = ["D", "C", "B", "A"]
    print()
    print("|\x1b[0;30;47m                                 Screen                                     \x1b[0m|")
    print()
    print()
    for i in range(len(normal_Seat)):
        print(normal[i] + " ", end="")
        for j in range(len(normal_Seat[i])):
            if normal_Seat[i][j] == "X":
                print(f"|\x1b[0;37;47m    \x1b[0m", end="")
            else:
                print(f"|\x1b[0;31;41m    \x1b[0m", end="")
        print()
        print()
    print()
    for q in range(len(honeymoon_Seat)):
        print(honeymoon[q] + " ", end="")
        for r in range(len(honeymoon_Seat[q])):
            if honeymoon_Seat[q][r] == "X":
                print(f"|\x1b[0;37;47m    \x1b[0m", end="")
            else:
                print(f"|\x1b[0;35;45m    \x1b[0m", end="")
        print()
        print()
    print("     1    2    3    4    5    6    7    8    9   10   11   12   13   14   15")
    print()
    print("                      \x1b[0;31;41m    \x1b[0m  220 Baht      \x1b[0;35;45m    \x1b[0m  240 Baht")

    return ""