import datetime

def date(value, format='medium'):
  # Create a python date object to work on
  date_obj = datetime.datetime.strptime(value, '%Y-%m-%d')
  if format == 'full':
    return date_obj.strftime("%m/%d/%Y")
  elif format == 'medium':
    return date_obj.strftime("%d-%b-%Y")

strTime = '2021-01-07'
print(date(strTime)) 