from cell import Cell

class Grid:
   def __init__(self, rows, columns):
      
      self.rows = rows
      self.columns = columns
      self.grid = []

   def print_grid(self):
      for row in self.grid:
         print('\n')
         for col in row:
            print(col.value, end=" ")
      print("\n")

   def edit_grid(self, position, new_value):
      x, y = position
      self.grid[x][y].value = new_value

   def create_grid(self):
      for row in range(self.rows):
         self.grid.append([])
         for col in range(self.columns):
            cell = Cell((row, col))
            self.grid[row].append(cell)