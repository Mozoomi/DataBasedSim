import pygame
import sys
from grid import Grid

pygame.init()

WIDTH, HEIGHT = 600, 600

rows, columns = HEIGHT//50, WIDTH//50
grid = Grid(rows, columns)
grid.create_grid()

canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World Sim")

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def draw_cell(value, position):
   x, y = position
   rectangle = pygame.Rect(x*50, y*50, 50, 50)

   if value == 0:
      pygame.draw.rect(canvas, BLUE, rectangle)
   elif value == 1:
      pygame.draw.rect(canvas, GREEN, rectangle)

#checks if it clicks on any cell
def get_clicked_cell(mouse_pol):
   for r in range(grid.rows):
      for c in range(grid.columns):
         cell_x = c * 50
         cell_y = r * 50
         if cell_x <= mouse_pol[0] < cell_x + 50 and cell_y <= mouse_pol[1] < cell_y + 50:
            return c, r
   return None

running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
         if event.button == 1:
            clicked_cell = get_clicked_cell(event.pos)
            if clicked_cell:
               print("DRAW: ", clicked_cell)
               grid.edit_grid(clicked_cell, 1)
         elif event.button == 3:
            clicked_cell = get_clicked_cell(event.pos)
            if clicked_cell:
               print("ERASE:", clicked_cell)
               grid.edit_grid(clicked_cell, 0)
      elif event.type == pygame.MOUSEMOTION:
         if pygame.mouse.get_pressed()[0]:
            hovered_cell = get_clicked_cell(event.pos)
            if hovered_cell:
               grid.edit_grid(hovered_cell, 1)
               print("HOLDING_DRAW: ", hovered_cell)
         elif pygame.mouse.get_pressed()[2]:
            hovered_cell = get_clicked_cell(event.pos)
            if hovered_cell:
               grid.edit_grid(hovered_cell, 0)
               print("HOLDING_ERASE: ", hovered_cell)
         
   #read grid
   for r in range(grid.rows):
      for c in range(grid.columns):
         draw_cell(grid.grid[r][c].value, grid.grid[r][c].position)
         
   #updates display every run
   pygame.display.flip()

pygame.quit()
sys.exit()