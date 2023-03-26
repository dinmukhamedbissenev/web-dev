def round_sum(a, b, c):
  return round_ten(a) + round_ten(b) + round_ten(c)


def round_ten(a):
  if(a == 0):
    return 0
  elif(a % 10 >= 5):
    return a + (10 - a%10)
  elif (a % 10 < 5):
    return a - a % 10
  
