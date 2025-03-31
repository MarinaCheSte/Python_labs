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