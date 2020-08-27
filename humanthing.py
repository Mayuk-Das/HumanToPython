import pyttsx3
import os

while True:
	print("chat with me with your requirements : "  , end='')
	p = input()

	if (("run" in p) or ("execute" in p ) or ("open" in p )or ("launch" in p )) and ("chrome" in p):
	  os.system("chrome")

	elif (("run" in p) or ("execute" in p ) or ("open" in p )or ("launch" in p )) and (("notepad" in p) or ("editor" in p)) :
	  os.system("notepad")

	elif (("run" in p) or ("execute" in p ) or ("open" in p )or ("launch" in p )) and (("player" in p) or ("media" in p)):
	  os.system("wmplayer")

	elif  (("exit" in p)  or ("quit" in p)):
	  break

	else:
	  print("dont support")