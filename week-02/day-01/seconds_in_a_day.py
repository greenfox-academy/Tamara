current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables
day_hours = 24
day_minutes = 00
day_seconds = 00

remaining_hours = day_hours - current_hours
remaining_minutes = day_minutes - current_minutes
remaining_seconds = day_seconds - current_seconds
remaining = remaining_hours*60*60 + remaining_minutes*60
remaining_total = remaining + remaining_seconds
remaining_total_var = int(remaining_total)
print( remaining_total_var ) 