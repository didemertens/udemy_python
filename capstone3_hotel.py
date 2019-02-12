'''
Airline / Hotel Reservation System - Create a reservation system which
books airline seats or hotel rooms. It charges various rates for particular
ections of the plane or hotel. Example, first class is going to cost more
than coach. Hotel rooms have penthouse suites which cost more. Keep track
of when rooms will be available and can be scheduled.

Start application
  > Start loop
Print welcome text
Show different rooms/prices
  > Show dictionairy of room/prices
User chooses room
  > Save choice
User input check-in/check-out dates
  > Run functions
  > Check availability for chosen room
Show total price for stay
  > Nights * room price
Ask if they want to book
  > Save room/dates or not
Print end text
Sleep for 3 seconds
Loop
'''

from datetime import *

class Rooms:

  def __init__(self):
    self.basic_room = {'Basic Room':50}
    self.family_room = {'Family Room' : 100}
    self.suite = {'Suite' : 150}

  def show_rooms(self):
    print(f"The Basic Room costs £{self.basic_room['Basic Room']} a night.")
    print(f"The Family Room costs £{self.family_room['Family Room']} a night.")
    print(f"The Suite costs £{self.suite['Suite']} a night.")

  def choice_room(self):
    user_choice = ''
    while True:
      user_input = input("\nPlease choose a room: ").lower()
      if 'basic' in user_input:
        user_choice = self.basic_room
        break
      elif 'family' in user_input:
        user_choice = self.family_room
        break
      elif 'suite' in user_input:
        user_choice = self.suite
        break
      else:
        print("Please enter a room from the list above.")
        continue
    return user_choice


'''
  def __init__(self, room, price):
    self.room = room
    self.price = price

  def __str__(self):
    return f"{self.room} costs {self.price} a night."


basic_room = Hotel('Basic room', 50)
print(basic_room.__str__())
'''


class BookingDates:

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
          print('We are going to check the availability!')
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


while True:
  print("Hello there! We're glad you've chosen Hotel California for your next trip.\nPlease view the below rooms and prices and make a choice.\n")
  room_booking = Rooms()
  room_booking.show_rooms()
  print(room_booking.choice_room())

  check_in_date = BookingDates.check_in_date()
  check_out_date = BookingDates.check_out_date(check_in_date)
  date_range = BookingDates.date_range(check_in_date,check_out_date)
  print(date_range)
  break










