from Movie import *
from Reservation import *
from cinema_print import *


movie_list = []
remaining_seat = []
reserved_list = []
booking_list = []

def movie():
    if len(movie_list) == 0:
        print("\nNo Movies")
    else:
        print("\nMovies Summary")
        for i in range(len(movie_list)):
            print(f"{i+1}.) {movie_list[i].get_movie()} {movie_list[i].get_seats()} seats")
    ans = input("\n     \033[95m(n)ew Movies\n     (d)elete movies\n     (m)ain menu\n     \033[00mChoose a menu : ")
    while ans != "m":
        if ans == "n" :
            movie = input("\nMovie name : ")
            print("Choose Theater Capacity")
            print(" >>> 100 Seats ")
            print(" >>> 120 Seats ")
            print(" >>> 150 Seats ")
            seats = int(input("Seat capacity : "))
            movie_list.append(Movie(movie,seats))
            remaining_seat.append(seats)
            booking_list.append([[],[],[],[]])
            print("\nMovies Summary")
            for i in range(len(movie_list)):
                print(f"{i+1}.) {movie_list[i].get_movie()} {movie_list[i].get_seats()} seats")
            #print(booking_list)
            ans = input("\n     \033[95m(n)ew Movies\n     (d)elete movies\n     (m)ain menu\n     \033[00mChoose a menu : ")
            #ans = input("\n     (n)ew Movies\n     (d)elete movies\n     (m)ain menu\n     Choose a menu : ")
        elif ans == "d" :
            print("\nMovies Summary")
            for i in range(len(movie_list)):
                print(f"{i+1}.) {movie_list[i].get_movie()} {movie_list[i].get_seats()} seats")
            delete  = int(input("\nMovie number : "))
            movie_list.remove(movie_list[delete-1])
            remaining_seat.remove(remaining_seat[delete-1])
            print("\nMovies Summary")
            for i in range(len(movie_list)):
                print(f"{i+1}.) {movie_list[i].get_movie()} {movie_list[i].get_seats()} seats")
            ans = input("\n     \033[95m(n)ew Movies\n     (d)elete movies\n     (m)ain menu\n     \033[00mChoose a menu : ")
            #ans = input("\n     (n)ew Movies\n     (d)elete movies\n     (m)ain menu\n     Choose a menu : ")


def booking():
    if len(movie_list) == 0:
        print("\nNo Movies")
    else :
        print("\nBookings Summary")
        for i in range(len(movie_list)):
            print(f"{i+1}.) {movie_list[i].get_movie()} {movie_list[i].get_seats()} seats Remaining {movie_list[i].get_seats()} seats")
        ans = input("\n     \033[94m(b)ook\n     (m)ain menu\n     \033[00mChoose a menu : ")
        while ans != "m":
            if ans == "b":
                name = input("\nName : ")
                movie = int(input("Movie : "))
                amount = int(input("Amount : "))
                cost = 0
                if movie_list[movie - 1].get_seats() == 100:
                    row_n = booking_list[movie - 1][0]
                    col_n = booking_list[movie - 1][1]
                    row_h = booking_list[movie - 1][2]
                    col_h = booking_list[movie - 1][3]
                    normal_Seat, honeymoon_Seat = seat_100(row_n, col_n, row_h, col_h)
                    print(print_cinema_100(normal_Seat, honeymoon_Seat))
                    n = 0
                    while n < amount :
                        s = input("(n)ormal or (h)oneymoon : ")
                        if s == "n":
                            row = translator_100(input("Row (E-J) : "))
                            booking_list[movie - 1][0].append(row)
                            col = int(input("Column (1-10) : "))
                            booking_list[movie - 1][1].append(col-1)
                            n += 1
                            cost += 220

                        elif s == "h":
                            row = translator_100(input("Row (E-J) : "))
                            booking_list[movie - 1][2].append(row)
                            col = int(input("Column (1-10) : "))
                            booking_list[movie - 1][3].append(col-1)
                            cost += 240
                            n += 1


                    row_n = booking_list[movie-1][0]
                    col_n = booking_list[movie-1][1]
                    row_h = booking_list[movie-1][2]
                    col_h = booking_list[movie-1][3]
                    normal_Seat, honeymoon_Seat = seat_100(row_n, col_n, row_h, col_h)
                    print(print_cinema_100(normal_Seat, honeymoon_Seat))
                    print(f"\x1b[0;34;40mTotal Price : {cost} Baht\x1b[0m")


                    #ans = input("\n     (b)ook\n     (m)ain menu\n     Choose a menu : ")


                elif movie_list[movie - 1].get_seats() == 120:
                    row_n = booking_list[movie - 1][0]
                    col_n = booking_list[movie - 1][1]
                    row_h = booking_list[movie - 1][2]
                    col_h = booking_list[movie - 1][3]
                    normal_Seat, honeymoon_Seat = seat_120(row_n, col_n, row_h, col_h)
                    print(print_cinema_120(normal_Seat, honeymoon_Seat))
                    n = 0
                    while n < amount :
                        s = input("(n)ormal or (h)oneymoon : ")
                        if s == "n":
                            row = translator_100(input("Row (E-J) : "))
                            booking_list[movie - 1][0].append(row)
                            col = int(input("Column (1-12) : "))
                            booking_list[movie - 1][1].append(col-1)
                            n += 1
                            cost += 220

                        elif s == "h":
                            row = translator_100(input("Row (E-J) : "))
                            booking_list[movie - 1][2].append(row)
                            col = int(input("Column (1-12) : "))
                            booking_list[movie - 1][3].append(col-1)
                            cost += 240
                            n += 1


                    row_n = booking_list[movie-1][0]
                    col_n = booking_list[movie-1][1]
                    row_h = booking_list[movie-1][2]
                    col_h = booking_list[movie-1][3]
                    normal_Seat, honeymoon_Seat = seat_120(row_n, col_n, row_h, col_h)
                    print(print_cinema_120(normal_Seat, honeymoon_Seat))
                    print(f"\x1b[0;34;40mTotal Price : {cost} Baht\x1b[0m")


                    #ans = input("\n     (b)ook\n     (m)ain menu\n     Choose a menu : ")

                elif movie_list[movie - 1].get_seats() == 150:
                    row_n = booking_list[movie - 1][0]
                    col_n = booking_list[movie - 1][1]
                    row_h = booking_list[movie - 1][2]
                    col_h = booking_list[movie - 1][3]
                    normal_Seat, honeymoon_Seat = seat_150(row_n, col_n, row_h, col_h)
                    print(print_cinema_150(normal_Seat, honeymoon_Seat))
                    n = 0
                    while n < amount :
                        s = input("(n)ormal or (h)oneymoon : ")
                        if s == "n":
                            row = translator_100(input("Row (E-J) : "))
                            booking_list[movie - 1][0].append(row)
                            col = int(input("Column (1-10) : "))
                            booking_list[movie - 1][1].append(col-1)
                            n += 1
                            cost += 220

                        elif s == "h":
                            row = translator_100(input("Row (E-J) : "))
                            booking_list[movie - 1][2].append(row)
                            col = int(input("Column (1-10) : "))
                            booking_list[movie - 1][3].append(col-1)
                            cost += 240
                            n += 1


                    row_n = booking_list[movie-1][0]
                    col_n = booking_list[movie-1][1]
                    row_h = booking_list[movie-1][2]
                    col_h = booking_list[movie-1][3]
                    normal_Seat, honeymoon_Seat = seat_150(row_n, col_n, row_h, col_h)
                    print(print_cinema_150(normal_Seat, honeymoon_Seat))
                    print(f"\x1b[0;34;40mTotal Price : {cost} Baht\x1b[0m")

                    #ans = input("\n     (b)ook\n     (m)ain menu\n     Choose a menu : ")








                reserved_list.append(Reservation(name,movie,amount))
                remaining_seat[movie-1] = (remaining_seat[movie-1]-amount)
                print("\nBookings Summary")
                for i in range(len(movie_list)):
                    print(f"{i+1}.) {movie_list[i].get_movie()} {movie_list[i].get_seats()} seats Remaining {remaining_seat[i]} seats")
                ans = input("\n     \033[94m(b)ook\n     (m)ain menu\n     \033[900mChoose a menu : ")


def report() :
    report_list = []
    name = input("\n\nName : ")
    message = input("Message\n")
    report_list.append([name,message])

    return  ""





print("\033[92m Welcome to Cinema !\033[00m")
print("--------------------")

print("\033[91m     Main menu      \033[00m\n")
main = "A"
while main != "e" :
    main = input("\n     \033[95m(m)ovies\033[00m\n     \033[94m(b)ookings\033[00m\n     \033[96m(r)eports\033[00m\n     \033[93m(e)xit\033[00m\n\n   Choose a menu : ")
    if main == "m" :
        movie()
    elif main == "b" :
        booking()
    elif main == "r" :
        report()

print("\n\n\033[91m      THANK YOU\033[00m")



