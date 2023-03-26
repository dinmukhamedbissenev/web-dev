def close_far(a, b, c):
  if (b == a + 1 or a - 1 or a) or (c == a + 1 or a - 1 or a):            
    if ((c > a + 2) and (c > b + 2)) or ((c <= a - 2) and (c <= b - 2)):   
        return True
    elif (b > (a + 2 and c + 2)) or ((b <= a - 2) and (b <= c - 2)):       
        return True
    else:    
      return False