from mutagen.mp3 import MP3 as mp3
import pygame

MUSIC_FILE = "./Anthem_of_the_Soviet_Union.mp3"

def main():
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_FILE)
    music_length = mp3(MUSIC_FILE).info.length

    while True:
        i = input("Type Start or Stop")
        if i == "Start" or i == "start":
            print("再生")
            pygame.mixer.music.play(1)
        elif i== "Stop" or i == "stop":
            print("停止")
            pygame.mixer.music.stop()

if __name__ == '__main__':
    main()
