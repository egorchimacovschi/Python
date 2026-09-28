import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.fps = 120
        self.running = True

        self.display_size = pygame.display.Info()

        self.monitor_width = self.display_size.current_w
        self.monitor_height = self.display_size.current_h

        self.screen_width = int(self.monitor_width * 0.8)
        self.screen_height = int(self.monitor_height * 0.8)


        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )
        pygame.display.set_caption("My Flappy Birds")


        self.ground_scroll = 0
        self.scroll_speed = 4

        self.background_img = pygame.image.load(
            "./data/img/bg.png"
        ).convert()
        self.background_img = pygame.transform.scale(self.background_img, (self.screen_width, self.screen_height))
        self.ground_img = pygame.image.load(
            "./data/img/ground.png"
        )
        self.ground_img = pygame.transform.scale(self.ground_img, (self.screen_width + self.screen_width * 0.04, self.screen_height * 0.1))

        
   
    def run(self):
        while self.running:

            self.screen.blit(self.background_img, (0, 0))
            self.screen.blit(self.ground_img, (self.ground_scroll, self.screen_height * 0.92))
            self.ground_scroll -= self.scroll_speed
            if abs(self.ground_scroll) > self.screen_width * 0.04:
                self.ground_scroll = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            pygame.display.flip()
            self.clock.tick(self.fps)


Game().run()