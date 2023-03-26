def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
  
def fix_teen(a):
  if(13 <= a <= 19 and a != 15 and a != 16):
    return 0
  else:
    return a
