from timeit import default_timer as timer

def unscramble(text):
  file = open('wordlist.txt','r')
  list = []
  lines = file.readlines()
  file.close()
  for line in lines: # search one line by one line
    count = len(text)
    if len(line.strip()) == len(text):
      for letter in text: # for each letter in the text
        if letter in line: # if a letter in the text matches a letter in the line
          count -= 1
    if count == 0:
      list.append(line.strip())
  print(list)


start = timer()
unscramble("abate")
end = timer()
print((end - start)*1000, "ms") # Time in ms