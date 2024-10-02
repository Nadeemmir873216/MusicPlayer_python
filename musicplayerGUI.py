import pygame
import os
import musicplayer as mp

pygame.init()
screen = pygame.display.set_mode((800, 600))

songs = mp.songs


class Button:
    def __init__(self, x, y, width, height, text, color = (255,255,255), font = pygame.font.SysFont("Arial",24)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.font = font

    def draw(self, screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
        text_surface = self.font.render(self.text,True,(68, 54, 60))
        # f"Clicks: {self.clicks}"
        screen.blit(text_surface,(self.x + 10,self.y +10))

    def is_clicked(self,mouse_pos):
        return (self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height)

def main():
    # songs = musicplayer.findSongs("songs", ".mp3")
    clock = pygame.time.Clock()
    
    backButton = Button(200,350,100,100,"<<",(183, 164, 172) , pygame.font.SysFont("Roboto Condensed Bold",100))
    pauseButton = Button (350,350,100,100,"^",(183, 164, 172) , pygame.font.SysFont("Roboto Condensed Bold",200))
    forwardButton = Button(500,350,100,100,">>",(183, 164, 172) , pygame.font.SysFont("Roboto Condensed Bold",100))
    text = Button(0,100,800,100,songs[0], (210, 198, 203),pygame.font.SysFont("Roboto Condensed Bold",50))
    
    index = 0
    paused = False

    player = mp.MusicPlayer()
    player.load(1)
    player.play()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.is_clicked(event.pos):
                    player.backward()
                    index -= 1
                    text.text = songs[index%len(songs)]
                if forwardButton.is_clicked(event.pos):
                    player.forward()
                    index +=1
                    text.text = songs[index%len(songs)]
                if pauseButton.is_clicked(event.pos):
                    if paused == False:
                        player.pause()
                        paused = True
                        pauseButton.text = "||"
                    else:
                        player.unpause()
                        paused = False
                        pauseButton.text = "^"

        
        screen.fill((210, 198, 203))
        backButton.draw(screen)
        forwardButton.draw(screen)
        text.draw(screen)
        pauseButton.draw(screen)
        pygame.display.update()
        clock.tick(60)

if len(songs)>0:
    if __name__ == "__main__":
        main()