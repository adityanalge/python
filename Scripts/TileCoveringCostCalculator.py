# -*- coding: utf-8 -*-
"""
Created on Sat May 12 23:26:04 2018

@author: adityanalge

Calculate the total cost of tile it would take to cover a floor plan of width and height, 
using a cost entered by the user.

"""

import os
flag = 0

def clear():
    os.system( 'cls' )
    
def roomSurfaceArea(width = 1, height = 1):
    return (2 * width * width) + (4 * width * height)

def tileArea(length = 1, width = 1):
    return length * width

def totalCost(num,temp):
    return (num * temp)

 
while True:
   
    print("Floor Plan Tile Cover Cost Calculator\n")
    
    Floor_Width = int(input("Enter Width of Floor in Feet\t"))
    Floor_Height = int(input("Enter Height of Floor in Feet\t"))
    print(f"\nSurface Area of room is {roomSurfaceArea(Floor_Width,Floor_Height)}\n")
    
    Tile_Length = int(input("Enter Length of Tile in Feet\t"))
    Tile_Width = int(input("Enter Width of Tile in Feet\t"))
    print(f"\nArea of each tile is {tileArea(Tile_Length,Tile_Width)}\n")
    
    numOfTiles = roomSurfaceArea(Floor_Width,Floor_Height)/tileArea(Tile_Length,Tile_Width)
    Tile_Cost = int(input("Enter Cost of Each Tile in Dollars\t"))
    print(f"\nTotal Cost is {totalCost(numOfTiles,Tile_Cost)} Dollars\n")
    
    flag = input("Enter 1 to run program again. Press any other key to terminate\t")
    
    if flag != '1':
        print("\nGoodbye!")
        break
    else:
        clear()
    