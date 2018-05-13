# -*- coding: utf-8 -*-
"""
Created on Sat May 12 23:26:04 2018

@author: adityanalge

Calculate the total cost of tile it would take to cover a floor plan of width and height, 
using a cost entered by the user.

"""
from IPython.display import clear_output

def tileArea(length = 1, width = 1):
    return length * width

def roomSurfaceArea(width = 1, height = 1):
    return (2 * width * width) + (4 * width * height)

def totalCost(tile_cost):
    return (roomSurfaceArea()/tileArea()) * tile_cost

 
while True:
    
    
    print("________________________________________________________________________________\n")
    print("Floor Plan Tile Cover Cost Calculator\n")
    
    Floor_Width = int(input("Enter Width of Floor in Feet\t"))
    Floor_Height = int(input("Enter Height of Floor in Feet\t"))
    
    Room_Area = roomSurfaceArea(Floor_Width,Floor_Height)
    print(f"\nSurface Area of room is {Room_Area}")
    
    Tile_Length = int(input("Enter Length of Tile in Feet\t"))
    Tile_Width = int(input("Enter Width of Tile in Feet\t"))
    
    Tile_Area = tileArea(Tile_Length,Tile_Width)
    print(f"\nArea of each tile is {Tile_Area}")
    
    Tile_Cost = int(input("Enter Cost of Each Tile in Dollars\t"))
    
    Total_Cost = totalCost(Tile_Cost)
    print(f"\nTotal Cost is {Total_Cost} Dollars")
    
    z = input("Enter 1 to run program again. Press any other key to terminate\t")
    
    if z != '1':
        print("\nGoodbye!")
        break
    else:
        clear_output()
    