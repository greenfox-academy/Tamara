# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52
a = 6
b = 52
c = 17
d = (a * c * 5)
print("coding_time: " + str(d))
e = c * b
f = float(d) / e
print("whole_working_hours: " + str(f * 100) + " %")
