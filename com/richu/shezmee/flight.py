
class Flight:

    def __init__(self,number , aircraft):
        if not number[:2].isalpha():
            raise ValueError(" No airline code in '{}' ".format(number))
        if not number[:2].isupper():
            raise ValueError(" Invalid airline code : '{}' ".format(number))
        self.aircraft = aircraft
        self.number = number

        rows , seats = aircraft.seating_plan()
        self.seating = [None] + [{seat:None for seat in seats} for _ in rows]

    def flightname(self):
        return self.number

    def flight_code(self):
        return  self.number[:2]

    def aircraft_registration(self):
        return self.aircraft.registration


class Aircraft:
    """Aircraft class"""
    def __init__(self ,  registration , model , num_rows , num_seat_per_row):
        self.registration = registration
        self.model = model
        self.num_rows = num_rows
        self.num_seats_per_row = num_seat_per_row


    def registration(self):
        return  self.registration

    def model(self):
        return  self.model



class FranceAir(Aircraft):
    """FranceAir class"""

    def seating_plan(self):
        return (range(1,self.num_rows + 1),'ABCDEFGHIJKL'[:self.num_seats_per_row])


class BritishAir(Aircraft):
    """BritishAir class"""

    def seating_plan(self):
        return (range(1,self.num_rows + 1),'MNOPQRSTUVW'[:self.num_seats_per_row])
