class Reservation :

    def __init__(self,name,movie,seat):
        self.__name = name
        self.__movie = movie
        self.__seat = seat

    def set_name(self,name):
        self.__name = name

    def set_movie(self,movie):
        self.__movie = movie

    def set_seat(self,seat):
        self.__seat = seat

    def get_name(self):
        return self.__name

    def get_seat(self):
        return self.__seat


    def __str__(self):
        return f"{self.__order}.) {self.__name}  {self.__movie}  {self.__seat} seats."


