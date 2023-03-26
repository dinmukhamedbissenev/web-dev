def diff21(n):
  if(n < 0):
    return abs(n - 21)
  elif(n > 21):
    return 2 * (n - 21)
  else:
    return 21 - n