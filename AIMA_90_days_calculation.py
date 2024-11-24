# This is the code that calculates the end date of 90-days period set forth for the reviewing residence permit application in Portugal

from datetime import datetime, timedelta

# Start date
start_date = datetime(2024, 10, 23)

# In Portugal, working days typically exclude weekends (Saturdays and Sundays)
# and public holidays. Assuming no holidays for simplicity.

# Calculate the number of days needed to get 90 working days (5 working days per week)
work_days = 90
current_date = start_date
days_passed = 0

while work_days > 0:
    # Check if the current day is a weekday (Monday=0, Sunday=6)
    if current_date.weekday() < 5:  # Weekday
        work_days -= 1
    current_date += timedelta(days=1)
    days_passed += 1

# The current_date will be the first non-working day after 90 working days, so subtract one day
end_date = current_date - timedelta(days=1)
print(end_date)
