#types of mode display
#check if user has typed in the right input

import time

#Displaying modes
def mode_run():
  print("Level 2:\nChoose one of these to start: ")
  print()
  print(" 1)Easy mode (level_1points)  \n minus 30 points for wrong answer \n Timer: 1 min(s) and 30 sec(s)")
  time.sleep(0.8)
  print("\n 2)Medium mode (level_1points)* 200 points  \n minus 80 points for wrong answer \n Timer: 60sec(s)")
  time.sleep(0.8)
  print("\n 3)Hard mode ((level_1points)* 500 points) \n minus 180 points for wrong answer \n Timer: 30sec(s)")
  time.sleep(0.9)
  print()
  print()
  return
  
#mode_run()
#loop trhoug response from user about what mode they choose

valid = True
while valid:
  
  error = "***   Whoops, type it again   ***"

  response = input("\n\nWhich Mode do you prefer? ").upper()
      
  if response == "EASY"  or response == "E" or response == "1":
    print("ACCEPTED")
    #valid = True
  elif response == "MEDIUM" or response == "M" or response == "2":
    print("ACCEPTED")
    #valid = True
  elif response == "HARD" or response == "H" or response == "3":
    print("ACCEPTED")
    #valid = True
  else:
    print(error)
    print()




  

