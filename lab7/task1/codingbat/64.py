def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if(a in b and b[len(b) - 1] == a[len(a) - 1]):
    return True
  elif(b in a and b[len(b) - 1] == a[len(a) - 1]):
    return True
  else:
    return False
