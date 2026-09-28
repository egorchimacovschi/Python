import pygame 

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.image_index = 0
        self.counter = 0

        for num in range(1, 4):
            img  = pygame.image.load(
                f"./data/img/bird{num}.png"
            )

            self.images.append(img)

        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        #handling the animation
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.image_index += 1
            if self.image_index >= len(self.images):
                self.image_index = 0
        self.image = self.images[self.image_index]

bird_group = pygame.sprite.Group()