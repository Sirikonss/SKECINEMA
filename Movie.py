class Movie :

    def __init__(self,movie = "",seats=0):
        self.__movie = movie
        self.__seats = seats

    def set_movie(self,movie):
        self.__movie = movie

    def set_seats(self,seats):
        self.__seats = seats

    def get_theater_id(self):
        return self.__theater_id

    def get_movie(self):
        return self.__movie

    def get_seats(self):
        return self.__seats



    def __str__(self):
        if self.__seats == 0 :
            return f"{self.__movie}"
        else:
            return f"{self.__movie} {self.__seats} seats"


