import sys
import pygame
import GameObject as GO
#import MoveableObject
#import Enemy
import Player as p

true = True
false = False

def setup():
    pygame.init() 
    pygame.font.init()

def run():
    screen = pygame.display.set_mode((640, 480))
    ImgList = [
        pygame.image.load("res/ProtagonistFace.PNG").convert(),
        pygame.image.load('res/Background.PNG').convert()
    ]

    player = p.Player(ImgList[0], [30, 260])
    background = GO.GameObject(ImgList[1], (320, 240))

    screen.blit(background.image, (0, 0))
    while true:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:# and not jumping:
                    jumping = true
                    player.jump(screen)

        screen.blit(background.image, background.pos)
        screen.blit(player.image, player.pos)
        pygame.display.update()

if __name__ == "__main__":
    setup()
    run()