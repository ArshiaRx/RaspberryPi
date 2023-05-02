#RPi = Rasbpberry Pi
#GPIO - General Purpose Input/Output
import RPi._GPIO as GPIO

#Delay
import time   

#Setting color in Hexadecimal
#          RED       GREEN    YELLOW     PURPLE   BLUE
COLOR = [0xFF0000, 0X00FF00, 0xFFFF00, 0xFF00FF, 0x00FFFF]

#Set pin's channel with dictionary
pins = {'Red' : 17, 'Green' : 18, 'Blue' : 27}

#===============================================================================================================================================
def setup():
    global p_R, p_G, p_B

    #BCM - Broadcom SOC channel
    GPIO.setmode(GPIO.BCM)

    #Set all LedPin's mode to output and set intial level to High (3.3V)
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT, initial = GPIO.HIGH)

    p_R = GPIO.PWM(pins['Red'], 2000)
    p_G = GPIO.PWM(pins['Green'], 2000)
    p_B = GPIO.PWM(pins['Blue'], 2000)
    
    p_R.start(0)
    p_G.start(0)
    p_B.start(0)
#=============================================================================================================================================
# Define a MAP function for mappinG values. Like from 0~255 to 0~100
def MAP(x, in_min, in_max, out_min,  out_max):
    return (x - in_min) * (out_max - out_min) / (in_max  - in_min) + out_min

#=============================================================================================================================================
# Define function to set up colors
def setColor(color):

# configures the three LED's luminance with the inputted color value.
    R_val = (color & 0xFF0000) >> 16
    G_val = (color & 0x00FF00) >> 8
    B_val = (color & 0x0000FF) >> 0
 
    # Map color value from 0~255 to 0~100
    R_val = MAP(R_val, 0, 255, 0, 100)
    G_val = MAP(G_val, 0, 255, 0, 100)
    B_val = MAP(B_val, 0, 255, 0, 100)

    # For example, a frequency can tell a Raspberry Pi system to switch an LED light on and off multiple times.
    # The data cycle informs the LED light how long it should remain illuminated before turning it back off.
    # In other words, the duty cycle tells the Raspberry Pi system how often the LED light should flash and for how long.
    
    # Change Color
    p_R.ChangeDutyCycle(R_val)
    p_G.ChangeDutyCycle(G_val)
    p_B.ChangeDutyCycle(B_val)

    print("\nColor_msg:\nR_val = %s\nG_val = %s\nB_val = %s"%(R_val, G_val, B_val))
#=============================================================================================================================================
def main():
    while True:
        for color in COLOR:
            setColor(color)  #Change the color of the RGB LED
            time.sleep(0.5)    # IN seconds Delay
#=============================================================================================================================================
def destroy():
    
    #STOP all terminal
    p_R.stop()
    p_G.stop()
    p_B.stop()

    #Release Source
    GPIO.cleanup()

#=============================================================================================================================================
if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
    

