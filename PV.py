# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:19:20 2024

@author: jjmcc
"""
#Create a class for solar panels
    #Allow for calculation of area of solar panel
    #Attributes - length, width, kWp
#Create a class for buildings and roofs
    #Allow for calculation of area of roof
    #Attributes - length, width, roof angle
#Calculate amount of panels per side and multiply by two
import math

class Building():
    def __init__(self, name, length, width, angle):
        self.name = name
        self.length = length
        self.width = width
        self.angle = angle
        self.roof_width = (self.width/2)/math.cos(self.angle*(math.pi/180))   
        
class Panel():
    def __init__(self, model_name, pv_length, pv_width, pv_power):
        self.model_name = model_name
        self.length = pv_length
        self.width = pv_width
        self.power = pv_power

      
building_name = input("Please provide the name of the building. ")
building_length = input("Please provide a value for the length of the building in metres.")
building_length = int(building_length)                 
building_width = input("Please provide a value for the width of the building in metres.")
building_width = int(building_width)
building_angle = input("Please input the angle of the roof in degrees")
building_angle = int(building_angle)
Building1 = Building(building_name, building_length, building_width, building_angle) 

pv_name = input("Please provide the model name of the panel.") 
panel_length = input("Please provide the length of the panel in mm.")
panel_length = int(panel_length)/1000
panel_width = input("Please provide the width of the panel in mm.")
panel_width = int(panel_width)/1000
panel_power = input("Please provide the peak power rating of the panel in W.")
panel_power = int(panel_power)/1000
Panel1 = Panel(pv_name, panel_length, panel_width, panel_power)

length_ratio = int(Building1.length/Panel1.length)
width_ratio = int (Building1.roof_width/Panel1.width)
panel_number = length_ratio*width_ratio*2
total_capacity = panel_number * Panel1.power

print(panel_number,total_capacity)

