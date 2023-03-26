def parrot_trouble(talking, hour):
  if(talking == True and (0 <= hour < 7 or 20 < hour <= 23)):
    return True
  else:
    return False
