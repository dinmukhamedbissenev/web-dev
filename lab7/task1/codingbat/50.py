def in1to10(n, outside_mode):
  if(outside_mode == False and 1 <= n <= 10):
    return True
  elif(outside_mode and  (n <= 1 or n >= 10)):
    return True
  else:
    return False
