import pygame as pg
import random as r

COLORS = [(255, 0, 0), (255, 153, 51), (255, 255, 102), (0, 255, 128), (0, 255, 255), \
          (255, 0, 255)]
SQ_COLOUR = (255, 102, 102)
COUNT = 0
MAG = 15
FRAME_MAG = 15
TEXT_SIZE = 35

class Player:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.square = game.square
        self.square_colour = SQ_COLOUR
        self.square.center = (300, 300)


    def draw(self):
        pg.draw.rect(self.screen, self.square_colour, self.square)


    def update_P(self):
        self.screen.fill((0, 0, 0))
        self.draw()


class Counter():
    def __init__(self, game):
        pg.font.init()
        self.screen = game.screen
        self.count = COUNT
        self.text_size = TEXT_SIZE
        self.shake_time = 0


    def display(self, count, text_size):
        r1 = r.randint(0, len(COLORS) - 1)
        font = pg.font.SysFont(None , text_size)
        img = font.render(f'Count: {count}', True, COLORS[r1])
        text_rect = img.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx  # Center horizontally
        text_rect.top = 20  # Place the text 20 pixels from the top

        if self.shake_time > 0:
            self.screenshake(text_rect)
        # Draw the text to the screen at the calculated position
        self.screen.blit(img, text_rect)


    def screenshake(self, text_rect):
        shake_x = r.randint(-MAG, MAG)
        shake_y = r.randint(-MAG, MAG)
        text_rect.x += shake_x
        text_rect.y += shake_y
        self.shake_time -= 1


class Game_Loop:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((600, 600))
        self.square = pg.Rect(0, 0, 100, 100)
        self.Player = Player(self)
        self.Counter = Counter(self)
        self.count = COUNT
        self.text_size = TEXT_SIZE

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.MOUSEBUTTONDOWN and self.square.collidepoint(pg.mouse.get_pos()):
                self.Player.square_colour = (255, 255, 255)
                self.count += 1
                self.text_size += 2
                self.Counter.shake_time = FRAME_MAG

            elif event.type == pg.MOUSEBUTTONUP and self.square.collidepoint(pg.mouse.get_pos()):
                self.Player.square_colour = (255, 102, 102)


    def run(self):
        while True:
            self.Player.update_P()
            self.check_events()
            self.Counter.display(self.count, self.text_size)
            pg.display.update()


if __name__ == "__main__":
    game = Game_Loop()
    game.run()