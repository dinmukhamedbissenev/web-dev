def squirrel_play(temp, is_summer):
  if(60 <= temp <= 90 and is_summer == False):
    return True
  elif(is_summer == True and 60 <= temp <= 100):
    return True
  else:
    return False
