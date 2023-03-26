def alarm_clock(day, vacation):
  if(vacation == False and 1 <= day <= 5):
    return '7:00'
  elif(vacation == False and (day == 0 or day == 6)):
    return '10:00'
  elif(vacation == True and 1 <= day <= 5):
    return '10:00'
  else:
    return 'off'
