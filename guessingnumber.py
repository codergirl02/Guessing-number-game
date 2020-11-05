n=11
guess=1
chance=1

while(chance<=5):
 guess=int(input("enter your guess: "))
 if(guess>11):
    print("you guessed the greater number")

 elif (guess<11):
    print("you guessed the lower number")
 else:
    print("congratulations!!! you are correct ")
    print(chance,"no. of guesses took to finish")
    break

 print(5 - chance,"no of guesses are left ")
 chance=chance+1

if(chance>5):
  print("you can guess number only 5 times....game over!")




