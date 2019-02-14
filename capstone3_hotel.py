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
    self.basic_room = {'Basic Room' : 50, 'Dates': [],}
    self.family_room = {'Family Room' : 100, 'Dates': [],}
    self.suite = {'Suite' : 150, 'Dates' : [],}

  def show_rooms(self):
    print(f"The Basic Room costs £{self.basic_room['Basic Room']} a night.")
    print(f"The Family Room costs £{self.family_room['Family Room']} a night.")
    print(f"The Suite costs £{self.suite['Suite']} a night.")

  def choice_room(self):
    user_choice = ''
    while True:
      user_input = input("\nPlease choose a room: ").lower()
      if 'basic' in user_input:
        user_choice = 'Basic room'
        break
      elif 'family' in user_input:
        user_choice = 'Family room'
        break
      elif 'suite' in user_input:
        user_choice = 'Suite'
        break
      else:
        print("Please enter a room from the list above.")
        continue
    return user_choice

  def dates_rooms(self, user_choice, date_range):
    if 'Basic' in user_choice:
      self.basic_room['Dates'].append(date_range)
    elif 'Family' in user_choice:
      self.family_room['Dates'].append(date_range)
    elif 'Suite' in user_choice:
      self.suite['Dates'].append(date_range)

# Plus, date range that isn't booked should be removed

  def available_rooms(self, user_choice, date_range):
    availability = True
    unique_list = []
    if 'Basic' in user_choice:
      for item in self.basic_room['Dates']:
        if item in unique_list:
          availability = False
        else:
          unique_list.append(item)
    elif 'Family' in user_choice:
      for item in self.baic_room['Dates']:
        if item in unique_list:
          availability = False
        else:
          unique_list.append(item)
    elif 'Suite' in user_choice:
      for item in self.suite['Dates']:
        if item in unique_list:
          availability = False
        else:
          unique_list.append(item)
    return availability


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


  # Print hello message, show rooms and ask for room choice
print("Hello there! We're glad you've chosen Hotel California for your next trip.")


room_booking = Rooms()

while True:
  print("\nPlease view the below rooms and prices and make a choice.\n")
  room_booking.show_rooms()
  user_choice = room_booking.choice_room()

  # Ask for room dates
  check_in_date = BookingDates.check_in_date()
  check_out_date = BookingDates.check_out_date(check_in_date)
  date_range = BookingDates.date_range(check_in_date,check_out_date)

  # Add the dates to dict. of room to be able to check for availability
  room_booking.dates_rooms(user_choice, date_range)
  availability = room_booking.available_rooms(user_choice, date_range)

  if availability == False:
    print("Sorry this room is unavailable.\n")
  else:
    print('Booked!\n')

  user_continue = input('Do you want to book another room? y/n ')
  if 'y' == user_continue[0].lower():
    continue
  elif 'n' == user_continue[0].lower():
    break










