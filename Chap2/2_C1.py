# Programmed by Mahdiyar Faqihi  { student_number :  14035191060 } { row :  24 }

import os
from mpmath import mp
from rich import print
from time import sleep


# mp.dps is the accuracy of mpmath library culculates, mp.dps >= 50 is for is good for high-precision calculations.
mp.dps = 50


# this function calculates the Rx.
def x_resultant(forces_magnitude: list, forces_angle: list):
    resultant = 0
    for i in range(len(forces_magnitude)):
        resultant += forces_magnitude[i] * float(mp.cos(mp.radians(forces_angle[i]))) # The Formula for vector decomposition on the X-Axis
    return resultant

#thid function calculates th Ry.
def y_resultant(forces_magnitude: list, forces_angle: list):
    resultant = 0
    for i in range(len(forces_magnitude)):
        resultant += forces_magnitude[i] * float(mp.sin(mp.radians(forces_angle[i]))) # The Formula for vector decomposition on the Y-Axis 
    return resultant

os.system("clear") # Clears the Terminal 
sleep(1)

magnitude_list = [] # Lists of Forces Magnitude
angle_list = [] # List of Forces Angle


# this loop is the main body of program (UI) 

while True:
    print("\n[italic][bold]Enter The Magnitude and Angle of Each Forces Step by Step[/bold][/italic].\n\n[bold][red]Tips[/red][/bold] :  Remember That Inputs the Angle Between Force and Positive Side of X-Axis\n\n")
    print("If the Inputs end, Enter 'q' in Magnitude of Force Section.\n\n")
    print("[bold]Entered Values[/bold]\n")
    print("Magnitude of Forces :  ", magnitude_list)
    print("Angle of Forces :  ", angle_list, "\n\n")

    magnitude = input("Enter The Magnitude of Force (Newton):  ") # The variable that inputs force magnitude

    if magnitude == 'q':  # if user enters 'q' in magnitude input, Variable input step Ends and the calculating part begins
        break
    
    try:
        magnitude = float(magnitude) # This checks that magnitude be a number not string
    except ValueError:
        print("\n[red][bold]Please enter a valid number for magnitude.[/bold][/red]")
        sleep(2)
        os.system("clear")
        sleep(1)
        continue

    angle = input("Enter the Angle of Force (Degree):  ")

    try: 
        angle = float(angle) # This checks that angle be a number not string  
    except ValueError:
        print ("\n[red][bold]Please enter a valid number.[/bold][/red]")
        sleep(2)
        os.system("clear")
        sleep(1)
        continue

    if angle > 180 or angle < -180: # The degree most be smaller than 180 or bigger than -180 for righ calculations 
        print("\n[red][bold]Please Enter Angles in The Right Way.[/bold][/red]")
        sleep(2)
        os.system("clear")
        sleep(1)
        continue

    magnitude_list.append(magnitude) # In these two lines we added the last force magnitude and angle to lists 
    angle_list.append(angle)

    os.system("clear") # clear terminal

os.system("clear")
sleep(1)

X = x_resultant(magnitude_list, angle_list) # We give magnitudes and angles to our main functions to decomposition Forces in X-Axis and Y-Axis
Y = y_resultant(magnitude_list, angle_list)

resultant_magnitude = round(mp.sqrt(mp.power(X, 2) + mp.power(Y, 2)), 4) # rounds manitude and angle of the resultant force to Number with four decimal places
resultant_angle = round(mp.degrees(mp.atan2(Y, X)), 4)

print(f"\nThe Resultant Force is a Vector With This Specifications :\n\nMagnitude : {resultant_magnitude} [italic]N[/italic]\nAngle : {resultant_angle} °\n\n\n")
