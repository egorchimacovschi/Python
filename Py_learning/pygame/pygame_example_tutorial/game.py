import pygame
import sys
from scripts.entities import  PhysicsEntity
from scripts.utils import load_image


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption('Ninja-Game')
        
        self.clock = pygame.time.Clock()

        self.collision_area = pygame.Rect(50, 50, 300 ,50)

        self.movement = [False, False]

        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
    
    def run(self):
        self.screen.blit(self.assets['player'], (100, 100))
        
        while True:
            self.screen.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False

            # update everything
            # draw all our elements
            pygame.display.update()
            self.clock.tick(60)
Game().run()
