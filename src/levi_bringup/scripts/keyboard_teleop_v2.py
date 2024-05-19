#from pynput import keyboard
#from pynput.keyboard import Key
from pyroombaadapter import PyRoombaAdapter
import math
import time
from time import sleep
import getch

#def on_key_release(key):
#    if key == Key.right:
#        print("Right key clicked")
#    elif key == Key.left:
#        print("Left key clicked")
#    elif key == Key.up:
#        print("Up key clicked")
#    elif key == Key.down:
#        print("Down key clicked")
#    elif key == Key.esc:
#        exit()


#with keyboard.Listener(on_release=on_key_release) as listener:
#    listener.join()

# Adapter setup
PORT = "/dev/ttyUSB0"
adapter = PyRoombaAdapter(PORT)


print("Keys: w, a, s, d")
#inp = input("Enter a key and then press ENTER: ")
start = time.time()


while True: # inp != "c":
    # print("RUNNING")
    inp = getch.getch()
    print(f"INPUT: {inp}")
    if inp == "c":
	    break
    elif inp == "a":
	    adapter.move(0, math.radians(20))
	    sleep(0.5)
    elif inp == "w":
	    adapter.move(0.2, math.radians(0.0))
	    sleep(0.5)
    elif inp == "s":
	    adapter.move(-0.2, math.radians(0.0))
	    sleep(0.5)
    elif inp == "d":
	    adapter.move(0, math.radians(-20))
	    sleep(0.5)
    else:
	    adapter.move(0, math.radians(0.0))
    adapter.move(0, math.radians(0.0))
    # inp = input()

adapter.move(0, math.radians(0.0))
