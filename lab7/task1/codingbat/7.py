def pos_neg(a, b, negative):
  if((a < 0 and b < 0 ) and negative == True):
    return True
  elif(a <0 and b < 0):
    return False
  elif( (a < 0 or b < 0) and negative == False):
    return True
  else:
    return False
