from pygame import *

w_window = 1000
h_window = 700

class gamesprite():
    def __init__(self, pl_image, pl_x, pl_y, pl_speed, pl_height, pl_widght):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (pl_height, pl_widght))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class rocket(gamesprite):
    def update_L(self):

        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed

    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

l_rocket = rocket('picture/line.png', 30, 100, 5, 30, 200)

r_rocket = rocket('picture/line.png', 940, 100, 5, 30, 200)

window = display.set_mode((w_window,h_window))
display.set_caption("ping pong")

clock = time.Clock()
FPS = 60

game = True
while game:



    window.fill((0, 179, 255))

    l_rocket.reset()
    l_rocket.update_L()

    r_rocket.reset()
    r_rocket.update_R()



    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
