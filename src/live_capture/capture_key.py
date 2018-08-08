##################################################
# Key Capturing                                  #
##################################################

# Library import
import keyboard

##################################################
# Callback method invoked each time a key is     #
# pressed                                        #
##################################################
def callback_keyPressed(event):
    print(event.name)

##################################################
# Method emulating key press                     #
##################################################
def pressKey(key):
    if key == 'up':
        keyboard.send('up')
    elif key == 'down':
        keyboard.send('down')
    elif key == 'left':
        keyboard.send('left')
    elif key == 'right':
        keyboard.send('right')
    else:
        pass

##################################################
# Hook key pressing event                        #
##################################################
keyboard.on_press(callback_keyPressed)

while 1:
    pass