# Source: https://www.redblobgames.com/grids/hexagons

class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

generate_cube = {
  'nw': lambda: Cube(-1, 0, +1),
  'ne': lambda: Cube(0, +1, -1),
  'n': lambda: Cube(-1, +1, 0),
  's': lambda: Cube(+1, -1, 0),
  'sw': lambda: Cube(0, -1, +1),
  'se': lambda: Cube(+1, 0, -1)
}

def cube_distance(a, b):
    return max(abs(a.x - b.x), abs(a.y - b.y), abs(a.z - b.z))

def cube_add(cube, d):
    return Cube(cube.x + d.x, cube.y + d.y, cube.z + d.z)

def cube_neighbor(cube, d):
    return cube_add(cube, generate_cube[d]())

def calculate_distance():
     with open('input') as f:        
        for line in f:
            coords = line.split(",")
        
     start = Cube(0,0,0)   
     end = start
     max_distance = -1
     for c in coords:
         end = cube_neighbor(end, c)
         distance = cube_distance(start, end)
         if (distance > max_distance):
             max_distance = distance
     
     print(max_distance)
     print(cube_distance(start, end))

calculate_distance()
