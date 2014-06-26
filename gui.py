import pygame
from pygame.locals import *
from basic_objects import MovingObject, Map

class App:
    def __init__(self):
        self._maze  = None
        self._moving_thing = None
        self._running = True
        self._image_black = None
        self._image_white = None
        self._image_mthing = None
        self._image_final = None
 
    def on_init(self):
        pygame.init()
        self._maze  = Map(10, 10)
        self._maze.recursive_division_maze_generation(1, 11, 1, 11)
        self._moving_thing = MovingObject(self._maze)
        self._display_surf = pygame.display.set_mode((1000, 700), pygame.HWSURFACE)
        self._running = True
        self._image_black = pygame.image.load("images/black.jpg").convert()
        self._image_white = pygame.image.load("images/white.jpg").convert()
        self._image_mthing = pygame.image.load("images/mthing.jpg").convert()
        self._image_final = pygame.image.load("images/final.jpg").convert()
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.on_key_down(event)
            elif event.key == pygame.K_w:
                self.on_key_up(event)
            elif event.key == pygame.K_a:
                self.on_key_left(event)
            elif event.key == pygame.K_d:
                self.on_key_right(event)

    def on_loop(self):
        pass

    def on_key_down(self, event):
        self._moving_thing.move_down()

    def on_key_up(self, event):
        self._moving_thing.move_up()

    def on_key_left(self, event):
        self._moving_thing.move_left()

    def on_key_right(self, event):
        self._moving_thing.move_right()

    def on_render(self):
        length = self._maze.length
        width = self._maze.width
        moving_thing = self._moving_thing
        for y in range(1, length + 1):              
            for x in range(1, width + 1):
                if abs(moving_thing.x - x) < 2 and abs(moving_thing.y - y) < 2:
                    if moving_thing.maze[x, y] == 0:
                        self._display_surf.blit(self._image_white,(x * 30,y * 30))
                        pygame.display.flip()
                    elif moving_thing.maze[x, y] == 1:
                        self._display_surf.blit(self._image_black,(x * 30,y * 30))
                        pygame.display.flip()
                    elif moving_thing.maze[x, y] == 2:
                        self._display_surf.blit(self._image_mthing,(x * 30,y * 30))
                        pygame.display.flip()
                    elif moving_thing.maze[x, y] == 3:
                        self._display_surf.blit(self._image_final,(x * 30,y * 30))
                        pygame.display.flip()
                elif moving_thing.maze[x, y] == 3:
                    self._display_surf.blit(self._image_final,(x * 30,y * 30))
                    pygame.display.flip()
                else:
                    self._display_surf.blit(self._image_black,(x * 30,y * 30))
                    pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()