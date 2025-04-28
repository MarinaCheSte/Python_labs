# 1. Создайте итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи
# и выведите эти числа.

class Iterate_tribonacci:
    def __init__(self, val):
        self.val = val

    def __iter__(self):
        return self._iter_generator()

    def _iter_generator(self):
        a, b, c = 0, 1, 1
        for _ in range(self.val):
            yield a
            a, b, c = b, c, a + b + c

iter_object = Iterate_tribonacci(35)

for i in iter_object:
    print(i)


# 2. Добавьте 5 магических метода к классу из предыдущего ДЗ.

#Kласс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
#Функции- члены реализуют запись и считывание полей (проверка корректности).
#Создать список объектов. Вывести:
#a)	список рейсов для заданного пункта назначения;
#б) список рейсов для заданного дня недели;.

class Airline:
    #Статические поля(переменные класса)
    flight_count=0

    #Динамические поля (перменные объекта)
    def __init__(self, destination, flight_number, aircraft_type, departure_time, weekday):
        self.destination=destination
        self.flight_number = flight_number
        self.__aircraft_type = aircraft_type #инкапсулированное поле тип самолета
        self.departure_time = departure_time
        self.weekday = weekday
        Airline.flight_count += 1

    # Магический метод №1 - строковое представление
    def __str__(self):
        return f"Airline(DESTINATION:{self.destination}, FLIGHT:{self.flight_number}, AIRCRAFT:{self.get_type()}, DEP_TIME:{self.departure_time}, WEEKDAY:{self.weekday})"

    # Магический метод №2  - оператор меньше

    def __lt__(self, other):
        return "YES"

    #Магический метод №3 - оператор больше
    def __gt__(self, other):
        return "YES"

    #Магический метод №4 -сложение, изменение времени в соответствии с часовым поясом
    def __add__(self, a):
        return self.departure_time+a

    #Магический метод №5 - вычитание, изменение времени в соответствии с часовым поясом
    def __sub__(self, a):
        return self.departure_time-a

    #Метод класса
    @classmethod
    def create_airline(cls, destination, flight_number, aircraft_type, departure_time, weekday ):
        return cls(destination, flight_number, aircraft_type, departure_time, weekday)

    #Метод объекта
    def show_info(self):
        return (f"Destination: {self.destination}, Flight number: {self.flight_number}, Aircraft type: {self.get_type()}, "
                f"Departure time: {self.departure_time}, Weekday: {self.weekday}")

   #Статический метод
    @staticmethod
    def get_flight_count():
        return Airline.flight_count

    #Сеттер и геттер для инкапсулированного поля

    def set_type(self, aircraft_type):
        if aircraft_type is not None:
            self.__aircraft_type = aircraft_type
        else:
            raise ValueError("Aircraft Type cannot be None")

    def get_type(self):
        return self.__aircraft_type

    #Создание списка объектов

airlines = [
    Airline("Tokyo", 11, "B", "12:20", "Monday"),
    Airline("New York", 22, "A", "22:30", "Tuesday"),
    Airline("Paris", 33, "C", "16:45", "Wednesday"),
    Airline("Paris", 44, "C", "13:15", "Friday"),
    Airline("Barcelona", 55, "D", "22:15", "Friday")
    ]

# Вывести список рейсов для заданного пункта назначения

flights_destination = [airline.show_info() for airline in airlines if airline.destination == "Paris"]
print("Flights to Paris:")
for flight in flights_destination:
    print(flight)

# Вывести список рейсов для заданного дня недели
flights_destination = [airline.show_info() for airline in airlines if airline.weekday == "Friday"]
print("Flights on Friday:")
for flight in flights_destination:
    print(flight)

# Магические методы - использование
# №1 строковое представление
AirlineString= Airline("Tokyo", 11, "B", "12:20", "Monday")
print(AirlineString)

# №2 оператор меньше (сравниеванием время отправления)

AirlineString1= Airline("Tokyo", 11, "B", "12.20", "Monday")
AirlineString2= Airline("Berlin", 12, "B", "13.20", "Monday")
AirlineString3= Airline("Tokyo", 11, "B", "12.00", "Monday")

print(AirlineString1.departure_time<AirlineString2.departure_time)

# №3 оператор больше (сравниваем номер рейса)
print(AirlineString1.flight_number>AirlineString2.flight_number)

#4 -сложение, изменение времени в соответствии с часовым поясом
x=float(AirlineString2.departure_time)
print('%.2f' % (x+2))

#5 - метод №5 - вычитание, изменение времени в соответствии с часовым поясом
x=float(AirlineString3.departure_time)
print('%.2f' % (x-2))
