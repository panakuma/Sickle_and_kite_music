import pygame
import RPi.GPIO as gpio

MUSIC_FILE = "./Anthem_of_the_Soviet_Union.mp3"

gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.IN)

comment = [""]


def main():
    pygame.mixer.init()

# キーボード操作してたときの名残
#    while True:
#        i = input("Type Start or Stop")
#        if i == "Start" or i == "start":
#            print("再生")
#            pygame.mixer.music.play(1)
#        elif i== "Stop" or i == "stop":
#            print("停止")
#            pygame.mixer.music.stop()

    base_status = gpio.HIGH
    previous_state = gpio.HIGH
    while True:
        if gpio.input(2) == gpio.LOW and previous_state != gpio.LOW:
            print("ソビエトロシアでは、プログラムがあなたを実行する！！")
            pygame.mixer.music.load(MUSIC_FILE)
            pygame.mixer.music.play(1)
            previous_state = gpio.LOW
        elif gpio.input(2) == gpio.HIGH and previous_state == gpio.LOW:
            pygame.mixer.music.stop()
            pygame.mixer.init()
            previous_state = gpio.HIGH


if __name__ == '__main__':
    main()
