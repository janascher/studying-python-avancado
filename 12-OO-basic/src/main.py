class AirplaneTrip:
    def __init__(self, origin, destiny):
        self.origin = origin
        self.destiny = destiny

    def __str__(self):
        return f"Viagem de {self.origin} para {self.destiny}"

    def __add__(self, other):
        return AirplaneTrip(self.origin, other.destiny)


airplane_trip_1 = AirplaneTrip("A", "B")
airplane_trip_2 = AirplaneTrip("B", "C")
airplane_trip_3 = airplane_trip_1 + airplane_trip_2

print(airplane_trip_1)  # imprime: Viagem de A para B
print(airplane_trip_2)  # imprime: Viagem de B para C
print(airplane_trip_3)  # imprime: Viagem de A para C
