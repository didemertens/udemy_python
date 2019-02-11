'''
Airline / Hotel Reservation System - Create a reservation system which
books airline seats or hotel rooms. It charges various rates for particular
ections of the plane or hotel. Example, first class is going to cost more
than coach. Hotel rooms have penthouse suites which cost more. Keep track
of when rooms will be available and can be scheduled.
'''

from datetime import *


class HotelBookings:

  def __init__self(self, room_type, nights):
    self.room_type = room
    self.nights = nights


    room_prices = {'Basic Room':50, 'Family Room':100, 'Suite':50}


# Ask for the check-in date
  def check_in_date():
    current_date = date.today()
    while True:
      try:
        d1, m1, y1= [int(x) for x in input('Enter your arrival date (dd-mm-yyyy): ').split('-')]
        check_in_date = date(y1,m1,d1)
        if check_in_date >= current_date:
          print('OK!')
          break
        else:
          print('Please use a valid date.')
          continue
      except ValueError:
        print('Please use the given format.')
        continue
    return check_in_date



# Ask for the check-out date
  def check_out_date(check_in_date):
    current_date = date.today()
    while True:
      try:
        d1, m1, y1= [int(x) for x in input('Enter your check-out date (dd-mm-yyyy): ').split('-')]
        check_out_date = date(y1,m1,d1)
        if check_out_date > check_in_date:
          print('Booked!')
          break
        else:
          print('Please use a valid date.')
          continue
      except ValueError:
        print('Please use the given format.')
        continue
    return check_out_date

  def date_range(date1, date2):
    date_range = []
    for date in range(int ((date2 - date1).days)+1):
      date_range.append(date1 + timedelta(date))
    return date_range



check_in_date = HotelBookings.check_in_date()
check_out_date = HotelBookings.check_out_date(check_in_date)
date_range = HotelBookings.date_range(check_in_date,check_out_date)
print(date_range)








