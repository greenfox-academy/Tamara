# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

N,line,c,p = 4,'','',1
spaces = ' '*N

for i in range(N):
  spaces = spaces[0:N-i]
  c = ''
  for j in range(p):
    c += "*"
  line += spaces+c+'\n'
  p += 2

print(line)
