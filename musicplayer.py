import pygame
import os
from pynput import keyboard


directory_path = 'songs'
extension = '.mp3'
paused = False


def findSongs(directory, extension):
    # List all files in the directory
    allfiles = os.listdir(directory)
    
    # Filter files with the specific extension
    songs = [file for file in allfiles if file.endswith(extension)]
    
    return songs

songs = findSongs(directory_path, extension)

class MusicPlayer:
    ind = 0
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def load(self, ind):
        self.ind = ind % len(songs)
        pygame.mixer.music.load(directory_path + '/' + songs[ind-1])

    def play(self):
        pygame.mixer.music.play(-1)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def forward(self):
        self.load(self.ind+1)
        self.play()

    def backward(self):
        self.load(self.ind-1)
        self.play()
 
def main():
    # FindSongs
    
    
    print(*songs , sep="\n")

    # Load and play the music file

    player = MusicPlayer()

    # screen = pygame.display.set_mode((800, 600))

    player.load(1)  
    player.play()
        
    def on_press(key):  # This keyboard event works without screen by another library ie pynput(keyboard) 
        global paused 
        if key == keyboard.Key.space:
            if paused == False : 
                player.pause()
                paused = True
            else : 
                player.unpause()
                paused = False             
        elif key.char == '.':
            player.forward()
        elif key.char == ',':
            player.backward()
        elif key== keyboard.Key.esc:
            player.stop()
            print("Music stopped.")
            return False  # Stops the listener

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if len(songs)>0:
    if __name__ == "__main__":
        main()
