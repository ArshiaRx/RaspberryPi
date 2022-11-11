import RPi.GPIO as GPIO
import time

LedPin = 17
def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    
    # Set LedPin's mode to output, and initial level to High (3.3V)
    GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)

# Define a main function for the main purpose
def main():
        while True:
            
            # Turn on LED
            print('... LED ON')
            GPIO.output(LedPin, GPIO.LOW)
            time.sleep(0.1)
            
            # Turn off LED
            print('LED OFF ...')
            GPIO.output(LedPin, GPIO.HIGH)
            time.sleep(0.33)
            
            
# Define a destroy function for clean up everything after the script finished
def destroy():
    # Turn off LED
    GPIO.output(LedPin, GPIO.HIGH)
    
    # Release resource
    GPIO.cleanup()
    
#if run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        main()
    # When 'ctrl+C' is pressed, the program destroy() will be executed.
    except keyboardInterrupt:
        destroy()
        
