import math

# Variable of x and y coordinates are assigned for each city
Atlanta_x, Atlanta_y = 33.74, -84.38
Orlando_x, Orlando_y = 28.53, -81.379
Savannah_x, Savannah_y = 32.08, -81.09
Charlotte_x, Charlotte_y = 35.22, -80.84
average_earth_radius = 6371.01 

# Variables are created for distance between cities
Atlanta_to_Savannah = average_earth_radius * math.acos(
    math.sin(math.radians(Atlanta_x)) 
  * math.sin(math.radians(Savannah_x)) 
  + math.cos(math.radians(Atlanta_x)) 
  * math.cos(math.radians(Savannah_x)) 
  * math.cos(math.radians(Atlanta_y - Savannah_y))) 

Atlanta_to_Charlotte = average_earth_radius * math.acos(
    math.sin(math.radians(Atlanta_x)) 
  * math.sin(math.radians(Charlotte_x)) 
  + math.cos(math.radians(Atlanta_x)) 
  * math.cos(math.radians(Charlotte_x)) 
  * math.cos(math.radians(Atlanta_y - Charlotte_y))) 

Atlanta_to_Orlando = average_earth_radius * math.acos(
    math.sin(math.radians(Atlanta_x)) 
  * math.sin(math.radians(Orlando_x)) 
  + math.cos(math.radians(Atlanta_x)) 
  * math.cos(math.radians(Orlando_x)) 
  * math.cos(math.radians(Atlanta_y - Orlando_y))) 

Savannah_to_Charlotte = average_earth_radius * math.acos(
    math.sin(math.radians(Savannah_x)) 
  * math.sin(math.radians(Charlotte_x)) 
  + math.cos(math.radians(Savannah_x)) 
  * math.cos(math.radians(Charlotte_x)) 
  * math.cos(math.radians(Savannah_y - Charlotte_y))) 

Orlando_to_Savannah = average_earth_radius * math.acos(
    math.sin(math.radians(Orlando_x)) 
  * math.sin(math.radians(Savannah_x)) 
  + math.cos(math.radians(Orlando_x)) 
  * math.cos(math.radians(Savannah_x)) 
  * math.cos(math.radians(Orlando_y - Savannah_y))) 

Savannah_to_Atlanta = average_earth_radius * math.acos(
    math.sin(math.radians(Savannah_x)) 
  * math.sin(math.radians(Atlanta_x)) 
  + math.cos(math.radians(Savannah_x)) 
  * math.cos(math.radians(Atlanta_x)) 
  * math.cos(math.radians(Savannah_y - Atlanta_y))) 

# calculates the sides of first triangle and then the area
side = (Atlanta_to_Savannah + Atlanta_to_Charlotte + Savannah_to_Charlotte) / 2
area_1 = (side * (side - Atlanta_to_Savannah) * (side - Atlanta_to_Charlotte) * (side - Savannah_to_Charlotte)) ** 0.5

# calculates the distances of second triangle and then the area
side = (Atlanta_to_Orlando + Orlando_to_Savannah + Savannah_to_Atlanta) / 2 
area_2 = (side * (side - Atlanta_to_Orlando) * (side - Orlando_to_Savannah) * (side - Savannah_to_Atlanta)) ** 0.5 

# calculates the total area of both triangles
area = area_1 + area_2

# prints result
print("The estimated area enclosed by the four cities is " + str(area))
