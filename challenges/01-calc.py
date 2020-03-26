# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
  calc = input("What calculation would you like to do? (add, sub, mult, div) \n")
  num1 = input("Input number one: \n")
  num2 = input("Input number two: \n ")
  if (calc == "add"):
    print(int(num1) + int(num2))
  elif (calc == "sub"):
    print(int(num1) - int(num2))
  elif (calc == "mult"):
    print(int(num1) * int(num2))
  elif (calc == "div"):
    print(int(num1) / int(num2))


calculator()