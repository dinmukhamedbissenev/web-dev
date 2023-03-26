def make_chocolate(small, big, goal):
  if(small + (big*5) < goal) or (goal % 5 > small):
    return -1
    
  if(big*5 < goal):
    return (goal - (big*5))

  return goal % 5