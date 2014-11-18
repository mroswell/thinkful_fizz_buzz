# fizzy.py

import sys

try:
  n = int(sys.argv[1])
except IndexError:
  n = raw_input("Enter something, yo!")
  n = int(n)
for i in range(1,n):
  if i % 15==0:
    print "fizz buzz"
  elif i % 3==0:
    print "fizz"
  elif i % 5 == 0:
    print "buzz"
  else:
    print i
