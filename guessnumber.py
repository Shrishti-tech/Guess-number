import random
target=random.randint(1,100)

while True:
  userChoice=input("Guess the target or Quit Q:")
  if(userChoice=="Q"):
    break
  userChoice=int(userChoice)
  if(userChoice==target):
    print("success")
    break
  elif(userChoice<target):
    print("your number is too small")
    
  else:print("your number is too big")



  
print("----gameover---")