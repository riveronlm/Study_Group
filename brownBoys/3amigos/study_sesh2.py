import datetime
import math


class Patient():

    def __init__(self, name, birthdate, height, blood):
        self.name = name
        self.birthdate = birthdate
        self.height = height
        self.blood = blood

    def Calc_Age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

    def height_Converter(self):
        in_cm = self.height
        in_feet = 0.0328*in_cm

        return round(in_feet, 2)


patient1 = Patient("Bobby", datetime.date(1992, 3, 12), 176, "A+")
patient2 = Patient("Bobby", datetime.date(1992, 3, 12), 176, "A+")

print("The patient age is: ", patient1.Calc_Age())
print("Patient height in feet is: ", patient1.height_Converter())

print(patient1.blood)
