import pygame
import sys
from grid import Grid

pygame.init()

WIDTH, HEIGHT = 600, 600

rows, columns = HEIGHT//50, WIDTH//50
grid = Grid(rows, columns)
grid.create_grid()

from input_events import InputEvents
colony_mode = False
inputEvents = InputEvents(grid)

canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World Sim")

#COLORS
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

def draw_cell(value, position):
   x, y = position
   rectangle = pygame.Rect(x*50, y*50, 50, 50)

   if value == 0:
      pygame.draw.rect(canvas, BLUE, rectangle)
   elif value == 1:
      pygame.draw.rect(canvas, GREEN, rectangle)
   elif value == 2:
      pygame.draw.rect(canvas, RED, rectangle)


running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
         inputEvents.button_click(event, colony_mode)
      elif event.type == pygame.MOUSEMOTION:
         inputEvents.button_hold(event, colony_mode)
      elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RETURN:
            colony_mode = True
   #read grid
   for r in range(grid.rows):
      for c in range(grid.columns):
         draw_cell(grid.grid[r][c].value, grid.grid[r][c].position)
         
   #updates display every run
   pygame.display.flip()

pygame.quit()
sys.exit()