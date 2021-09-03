# main.py

morseDict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}

def morseText(msg):
  morseMsg = ""
  for letter in msg:
    if letter == " ":
      morseMsg += "   "
    else:
      morseMsg += morseDict[letter] + " "
  return morseMsg
  
msg = input("Type in a message to translate into morse code (in all lowercase): ")     

print("\n" + morseText(msg))
