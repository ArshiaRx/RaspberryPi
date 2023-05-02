from pygame import mixer
import RPi.GPIO as GPIO
import time

#ButtonPin number
#set the initial volume to 0.7.
BtnPin1 = 18  #Pause/play the music
BtnPin2 = 17  #Down volume
BtnPin3 = 27  #Up volume
volume = 0.7  

status = False
upPressed = False
downPressed = False
playPressed = False

def setup():
	mixer.init()
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BtnPin1, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(BtnPin2, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(BtnPin3, GPIO.IN, GPIO.PUD_UP)

def clip(X,min,max):
    if X < min:    
        return min
    elif X > max:  
        return max
    return X

def play(pin):
    global playPressed 
    playPressed = True 

def volumeDown(pin):
    global downPressed 
    downPressed = True

def volumeUp(pin):
    global upPressed 
    upPressed = True

def main():
	global volume, status
	global downPressed, upPressed, playPressed
	mixer.music.load('/home/matrix/Downloads/Sam-Smith-Unholy.mp3')   #Directory address
	mixer.music.set_volume(volume)
	mixer.music.play()
	GPIO.add_event_detect(BtnPin1, GPIO.FALLING, callback=play)
	GPIO.add_event_detect(BtnPin2, GPIO.FALLING, callback=volumeDown)
	GPIO.add_event_detect(BtnPin3, GPIO.FALLING, callback=volumeUp)
	while True:
		if upPressed:
			volume += 0.1
			upPressed = False

		if downPressed:
			volume -= 0.1
			downPressed = False

		if playPressed:
			if status:
				mixer.music.pause()        #when pressed, pause the music
				status = not status

			else:
				mixer.music.unpause()      #when pressed, play the music back
				status = not status
			playPressed = False
			time.sleep(0.5)
		volume = clip(volume, 0.2, 1)
		mixer.music.set_volume(volume)
		time.sleep(0.1)    

def destroy():
	# Release thee resource
	GPIO.cleanup()
	mixer.music.stop()


# Do this if running this script directly
if __name__ == '__main__':
	setup()
	try:
		main()
	# When 'Ctrl + c' is pressed, the program
	# destroy() will be executed

	except KeyboardInterrupt:
		destroy()