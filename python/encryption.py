crypt = {
  "q":"a",
  "w":"s",
  "e":"d",
  "r":"f",
  "t":"g",
  "y":"h",
  "u":"j",
  "i":"k",
  "o":"l",
  "p":";",
  "z":"q",
  "x":"w",
  "c":"e",
  "v":"r",
  "b":"t",
  "n":"y",
  "m":"u",
  "a":"!",
  "s":"@",
  "d":"#",
  "f":"$",
  "g":"%",
  "h":"^",
  "j":"&",
  "k":"*",
  "l":"("
}

def encrypt(text):
  encrypted=""
  for letter in text:
    if letter in crypt:
      encrypted += crypt[letter.lower()]
    else:
      encrypted += letter
  print(encrypted)
  return encrypted

def decrypt(text):
  decrypted=""
  items = crypt.items()
  for letter in text:
    found = False
    for target in items:
      if target[1] == letter:
        decrypted += target[0]
        found = True
        break
    if found == False:
      decrypted += letter
  print(decrypted)
  return decrypted

decrypt(encrypt("Hi, my name is Tommy"))
decrypt(encrypt("The Whale"))
# first output is encrypted, second one is decrypted.
