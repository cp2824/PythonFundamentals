"""
Model for aircraft flights
"""
import string
from pprint import pprint as pp

class Flight:

    def __init__(self, number, aircraft):
        # 1) Pos 0-1 must be capital letters
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code in '{}'".format(number))
        # 2) Pos 2-5 must be digits and 0 < int < 999
        if not number[2:].isdigit() and int(number[2:]) <= 999:
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        # list of Dictionaries
        # Waste one entry to match the actual number from the map
        # To the single element list, concatenate another list containing one entry for each row in the aircraft.
        # Done by the list comprehension from the list of rows retrieve from the seating plan.
        # Discard the row number (_) since you already have it from before.
        # the item from the comprehension is itself a dictionary comprehension
        # Use the list comprehension because we want a distinct object for each row.
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        """
        Parse a seat designated into a valid row and letter
        :param seat: A seat designator such as '12A'
        :return: a tupple with seat number and row
        """
        letter = seat[-1]
        rows, seat_letter = self._aircraft.seating_plan()
        # validate letter
        if letter not in seat_letter:
            raise ValueError("Invalid seat letter{}".format(letter))
        # validate row format
        row_text = seat[:-1]
        try:
            row_number = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row{}".format(row_text))
        # valid row?
        if row_number not in rows:
            raise ValueError("Invalid row number{}".format(row_number))

        #if self._seating[row_number][letter] is not None:
        #    raise ValueError("Seat {} is already occupied".format(seat))

        return row_number, letter

    def allocate_seats(self, seat, passenger):
        """
        Allocate a seat to a passenger
        :param seat: A seat designator such as '12A', '21F'
        :param passenger: The passenger name
        :return: ValueError: if the seat is unavailable
        """

        row, letter = self._parse_seat(seat)

        self._seating[row][letter] = passenger

    def reallocate_passengers(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to reallocate in seat{}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))
        # Assign new seat and clear old seat
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


    def num_availabe_seats(self):
        """
        Returns available seats
        :return: Available seats
        """

        return sum(sum(1 for s in row.values() if s is None)
                for row in self._seating if row is not None)


    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))

class Aircraft:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class AirbusA319 (Aircraft):
    def model(self):
        return "Airbus 318"

    def seating_plan(self):
        return range(1,23), "ABCDEF"


class Boeing777:
    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1, 56), "ABCDEFGHJ"

def console_card_printer(passenger, seat, flight_number, aircraft):
    """
    Prints the ticket
    :param passenger:
    :param seat:
    :param flight_number:
    :param aircraft:
    :return:
    """
    output = "| Name: {0}"\
             "  Flight: {1}"\
             "  Seat: {2}"\
             "  Aircraft: {3}"\
             "|".format(passenger, flight_number, seat, aircraft)
    banner = "+"
    border = "|"
    middle = border + " "*(len(output)-2) + border
    bottom = banner + "-"*(len(output)-2) + banner
    lines = [bottom, middle, output, middle, bottom]
    card = '\n'.join(lines)
    print(card)
    print()

def fill_plane():
    #a = Aircraft("AA777", "AirBus A319", num_rows=22, num_seats_per_row=6)
    #print(a.registration())
    #print(a.model())
    #print(a.seating_plan())

    f = Flight("AA777", AirbusA319("G-EUPT"))
    #print(f.number())
    #print(f.airline())
    #print(f.aircraft_model())

    g = Flight("AB123", Boeing777("Test"))
    f.allocate_seats("12A", "Guido van Rossum")   # father of Python
    f.allocate_seats("12B", "Rasmus Lerdorf")     # php
    g.allocate_seats("15F", "Bjarne Stroustrup")  # c++
    f.allocate_seats("15E", "Anders Hejlsberg")   # Turbo Pascal
    g.allocate_seats("22E", "Yukihiro Matsumoto") # Ruby

    return f, g

def main():
    """

    :return:
    """

    f, g = fill_plane()
    g.reallocate_passengers("22E", "12C")

    pp(f._seating)
    print(f.num_availabe_seats())

    pp(g._seating)
    print(g.num_availabe_seats())

    #console_card_printer("Guido", "DD782", "22A", "Boeing 747")
    # pass the function as a parameter, not with the parenthesis or python will try to execute the function.
    f.make_boarding_cards(console_card_printer)


if __name__ == '__main__':
    main()