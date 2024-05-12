import pygame

class InputEvents:
  def __init__(self, grid):
    self.grid = grid

  #checks if it clicks on any cell
  def get_clicked_cell(self, mouse_pol):
     for r in range(self.grid.rows):
        for c in range(self.grid.columns):
           cell_x = c * 50
           cell_y = r * 50
           if cell_x <= mouse_pol[0] < cell_x + 50 and cell_y <= mouse_pol[1] < cell_y + 50:
              return c, r
     return None
  
  def button_click(self, event, colony_mode):
    if event.button == 1:
      clicked_cell = self.get_clicked_cell(event.pos)
      x, y = clicked_cell
      if clicked_cell:
        print("DRAW: ", clicked_cell)
        if colony_mode and self.grid.grid[x][y].value == 1:
          self.grid.edit_grid(clicked_cell, 2)
        elif colony_mode != True:
          self.grid.edit_grid(clicked_cell, 1)
    elif event.button == 3:
      clicked_cell = self.get_clicked_cell(event.pos)
      x, y = clicked_cell
      clicked_cell_value = self.grid.grid[x][y].value
      if clicked_cell_value == 2:
        if colony_mode:
          self.grid.edit_grid(clicked_cell, 1)
      elif clicked_cell_value == 1:
        if not colony_mode:
          self.grid.edit_grid(clicked_cell, 0)
      print("ERASE:", clicked_cell)
        
  
  def button_hold(self, event, colony_mode):
    if pygame.mouse.get_pressed()[0] and colony_mode != True:
      hovered_cell = self.get_clicked_cell(event.pos)
      if hovered_cell and colony_mode != True:
        self.grid.edit_grid(hovered_cell, 1)
        print("HOLDING_DRAW: ", hovered_cell)
    elif pygame.mouse.get_pressed()[2]:
      hovered_cell = self.get_clicked_cell(event.pos)
      x, y = hovered_cell
      hovered_cell_value = self.grid.grid[x][y].value
      if hovered_cell_value == 1:
        if colony_mode:
          pass
        else:
          self.grid.edit_grid(hovered_cell, 0)
      elif hovered_cell_value == 2:
        if colony_mode:
          self.grid.edit_grid(hovered_cell, 1)
      print("HOLDING_ERASE: ", hovered_cell)