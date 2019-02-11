'''
Airline / Hotel Reservation System - Create a reservation system which
books airline seats or hotel rooms. It charges various rates for particular
ections of the plane or hotel. Example, first class is going to cost more
than coach. Hotel rooms have penthouse suites which cost more. Keep track
of when rooms will be available and can be scheduled.
'''

from datetime import *


class Hotel:

  def __init__self(self, room_type, nights):
    self.room_type = room
    self.nights = nights


    room_prices = {'Basic Room':50, 'Family Room':100, 'Suite':50}


# Ask arrival date
  def arrival_date():
    arrival_dates = []
    current_date = date.today()
    while True:
      try:
        d1, m1, y1= [int(x) for x in input('Enter your arrival date (dd-mm-yyyy): ').split('-')]
        guest_date = date(y1,m1,d1)
        # guest_month = int(input('Enter the month (mm): '))
        # # # guest_day = int(input('Enter the day (dd): '))
        # # # guest_date = datetime.strptime(guest_year, guest_month, guest_day)
        if guest_date == current_date:
          arrival_dates.append(guest_date)
          break
        elif guest_date > current_date:
          arrival_dates.append(guest_date)
          break
        else:
          print('Not a valid date.')
          continue
      except ValueError:
        print('Please enter a valid date.')
        continue
    return arrival_dates


# Ask the amount of nights
  def amount_nights():
    guest_nights = input('How many nights do you want to stay? ')


print(Hotel.arrival_date())





