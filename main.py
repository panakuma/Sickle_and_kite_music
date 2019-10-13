import pygame
import RPi.GPIO as gpio

MUSIC_FILE = "./Anthem_of_the_Soviet_Union.mp3"

gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.IN)

def main():
    previous_state = gpio.HIGH
    while True:
        if gpio.input(2) == gpio.LOW and previous_state != gpio.LOW:
            print("ソビエトロシアでは、プログラムがあなたを実行する！！")
            pygame.mixer.init()
            pygame.mixer.music.load(MUSIC_FILE)
            pygame.mixer.music.play(1)
            previous_state = gpio.LOW
        elif gpio.input(2) == gpio.HIGH and previous_state == gpio.LOW:
            pygame.mixer.music.stop()
            previous_state = gpio.HIGH

if __name__ == '__main__':
    main()
