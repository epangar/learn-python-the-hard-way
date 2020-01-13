i = 0
numbers = []

while i < 6:
  print "At the top i is %d" % i
  numbers.append(i)

  i = i + 1
  print "Numbers now: ", numbers
  print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
  print num


def print_pyramid(base):
  j=0
  while j < base:
    print "*" * (j+1)
    j += 1

print_pyramid(6)