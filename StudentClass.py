from datetime import date

today = date.today()
year = today.year


class StudentClass:
    def __init__(self, stu_id, name, birth, classification):
        self.__stu_id = stu_id
        self.__name = name
        self.__birth = birth
        self.__dob = "10/11/2001"
        self.__classification = classification
        self.__age = 0
        self.__register = ""

    def calc_age(self):
        today = date.today()
        date_birth = self.__dob.split("/")
        self.__age = today.year - int(date_birth[2])

    def calc_register(self):
        if self.__classification == "senior":
            self.__register = "4/1 thru 4/3"
        elif self.__classification == "junior":
            self.__register = "4/4 thru 4/6"
        elif self.__classification == "sophmore":
            self.__register = "4/7 thru 4/9"
        elif self.__classification == "freshman":
            self.__register = "4/10 thru 4/12"
        else:
            self.__register = "classification not found"

    def get_age(self):
        return self.__age

    def get_register(self):
        return self.__register
