from capstone3_hotel import *

check_in_date = BookingDates.check_in_date()
check_out_date = BookingDates.check_out_date(check_in_date)
date_range = BookingDates.date_range(check_in_date,check_out_date)
print(date_range)
