import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()



        self.display_size = pygame.display.Info()
        self.monitor_width = self.display_size.current_w
        self.monitor_height = self.display_size.current_h

        self.screen_width = int(self.monitor_width * 0.8)
        self.screen_height = int(self.monitor_height * 0.8)

        self.bird_pos = [self.screen_width * 0.2, self.screen_height * 0.5]
        self.bird_velocity = 0
        self.gravity = 0.7
        self.flap_strength = -16
        

        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )

        self.ground_height_ratio = 0.03 # tweak based on how tall the grass looks in your image
        self.ground_rect = pygame.Rect(
            0,
            int(self.screen_height * (1 - self.ground_height_ratio)),
            self.screen_width,
            int(self.screen_height * self.ground_height_ratio),
        )
        self.ceiling_rect = pygame.Rect(0, -50, self.screen_width, 1)


        self.original_background = pygame.image.load(
            "./data/background/background.png"
        ).convert()
        self.bird_image = pygame.image.load(
            "./data/sprites/bird/bird.png"
        ).convert_alpha()
        self.bird_radius = self.bird_image.get_width() //2

        self.background = pygame.transform.scale(
            self.original_background, (self.screen_width, self.screen_height)
        )

        self.icon = pygame.image.load("./data/icon/icon.png").convert_alpha()

        pygame.display.set_caption("My Flappy Birds")
        pygame.display.set_icon(self.icon)

        self.clock = pygame.time.Clock()
        self.running = True
   
    def run(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(
                self.bird_image,
                (
                    int(self.bird_pos[0] - self.bird_image.get_width() / 2),
                    int(self.bird_pos[1] - self.bird_image.get_height() / 2),
                )
            )

            bird_rect = self.bird_image.get_rect(
                center=(int(self.bird_pos[0]), int(self.bird_pos[1]))
            )

            if bird_rect.colliderect(self.ground_rect):
                self.bird_pos[1] = self.ground_rect.top - self.bird_radius
                self.bird_velocity = 0
                print("Hit the ground!")

            if bird_rect.colliderect(self.ceiling_rect):
                self.bird_pos[1] = self.ceiling_rect.bottom + self.bird_radius
                self.bird_velocity = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird_velocity = self.flap_strength

            self.bird_velocity += self.gravity
            self.bird_pos[1] += self.bird_velocity

            pygame.display.flip()
            self.clock.tick(120)


Game().run()