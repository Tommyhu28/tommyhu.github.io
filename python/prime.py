def prime_list():
  numbers = int(input(), 10)
  list = []
  count = 2
  while count < numbers:
    number = int(count/2)
    flag = False
    while number > 1:
      if count%number == 0:
        flag = True
        break
      number -= 1
    if flag is False:
      list.append(count)
    count += 1
  print(list)

prime_list()