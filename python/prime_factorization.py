def prime_list(number): # slightly modified from prime.py
  list = []
  count = 2
  while count < number:
    a = int(count/2)
    flag = False
    while a > 1:
      if count%a == 0:
        flag = True
        break
      a -= 1
    if flag is False:
      list.append(count)
    count += 1

  return list

def prime_fact(number):
  list = prime_list(number) # fetch prime list using previously constructed function in prime.py
  res_list = []
  for divisor in list:
    while (number%divisor==0):
      res_list.append(divisor)
      number /= divisor
    if (number==1): break
  print(res_list)
  return res_list

prime_fact(228)