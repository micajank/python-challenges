print("Welcome to Chase bank.")


balance = 4000
def depo(bal):
  value = input("How much would you like to deposit?\n")
  bal += int(value)
  return bal

def withd(b):
  value2 = input("How much would you like to withdraw?\n")
  b -= int(value2)
  return b

def bank(balance):
  print(f"Your current ballance is {balance}")
  choice = input("What would you like to do? (deposit, withdraw, check_balance)\n")
  if (choice == "deposit"):
    depo(balance)
  elif (choice == "withdraw"):
    withd(balance)
  print(f"Your current balance is {balance}")
  ask = input("are you done? ")
  if (ask == "yes"):
    print("Thank you")
  else:
    bank(balance)
  

bank(balance)