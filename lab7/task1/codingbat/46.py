def caught_speeding(speed, is_birthday):
  if(is_birthday and speed <= 65 or (is_birthday == False and speed <= 60)):
    return 0
  elif(is_birthday == False and 61<= speed <= 80 or (is_birthday and 66 <= speed <= 85)):
    return 1
  else:
    return 2
