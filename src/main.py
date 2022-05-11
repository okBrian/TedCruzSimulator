import sys
import pygame
import GameObject as GO
#import MoveableObject
#import Enemy
import Player as p

true = True

def setup():
    pygame.init() 
    pygame.font.init()

def run():
    screen = pygame.display.set_mode((640, 480))
    playerImg = pygame.image.load("res/ProtagonistFace.PNG").convert()
    backgroundImg = pygame.image.load('res/Background.PNG').convert()
    player = p.Player(playerImg, (320, 240))
    background = GO.GameObject(backgroundImg, (320, 240))

    screen.blit(background.image, (0, 0))
    while true:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background.image, background.pos, background.pos)
        screen.blit(player.image, player.pos)
        pygame.display.update()
        pygame.time.delay(100)

if __name__ == "__main__":
    setup()
    run()