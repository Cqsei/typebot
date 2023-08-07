import pynput
import random 
import threading
import time
import configparser
import sys
import keyboard

# Read values from the INI file
config = configparser.ConfigParser()
config.read("config.ini")

speed = config.getfloat('DEFAULT', 'speed', fallback=0.1)
time_delay = config.getfloat('DEFAULT', 'time_delay', fallback=5)
range1 = config.getfloat('RANGE', 'range1', fallback=0.1)
range2 = config.getfloat('RANGE', 'range2', fallback=0.3)

f = open("text.txt", "r")
txt = f.read()

class Sim_keyb_typing(threading.Thread):
    
    def __init__(self, text, 
                 strt_delay=time_delay, 
                 dct_delays={('a','i'):0.1}, 
                 delayrange=(speed, speed) ):
        threading.Thread.__init__(self)

        self.text = text
        self.strt_delay = strt_delay
        self.last_char = " "
        self.dct_delays = dct_delays
        self.delayrange = delayrange

        self.ppkbC = pynput.keyboard.Controller()

    def run(self):
        time.sleep(self.strt_delay)
        for char in self.text:
            delay = self.dct_delays.get( 
                (self.last_char, char), random.uniform(self.delayrange[0], self.delayrange[1]) )
            time.sleep(delay)
            self.ppkbC.type(char)
            self.last_char = char
            speed_delay = random.uniform(self.delayrange[0], self.delayrange[1])
            time.sleep(speed_delay)

    while True:
        if keyboard.is_pressed("ctrl+f8"):
            sys.exit()

# Let's wait 1.5 seconds and then start typing:
skt = Sim_keyb_typing(txt, time_delay)
skt.start()
# Wait for Sim_keyb_typing(txt) to finish
#skt.join()
