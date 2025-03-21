import os
from mpmath import mp
from rich import print
from time import sleep

mp.dps = 50

def x_resultant(forces_magnitude: list, forces_angle: list):
    resultant = 0
    for i in range(len(forces_magnitude)):
        resultant += forces_magnitude[i] * float(mp.cos(mp.radians(forces_angle[i])))
    return resultant

def y_resultant(forces_magnitude: list, forces_angle: list):
    resultant = 0
    for i in range(len(forces_magnitude)):
        resultant += forces_magnitude[i] * float(mp.sin(mp.radians(forces_angle[i])))
    return resultant

os.system("clear")
sleep(1)

magnitude_list = []
angle_list = []

while True:
    print("\n[italic][bold]Enter The Magnitude and Angle of Each Forces Step by Step[/bold][/italic].\n\n[bold][red]Tips[/red][/bold] :  Remember That Inputs the Angle Between Force and Positive Side of X-Axis\n\n")
    print("If the Inputs end, Enter 'q' in Magnitude of Force Section.\n\n")
    print("[bold]Entered Values[/bold]\n")
    print("Magnitude of Forces :  ", magnitude_list)
    print("Angle of Forces :  ", angle_list, "\n\n")

    magnitude = input("Enter The Magnitude of Force (Newton):  ")

    if magnitude == 'q':
        break
    
    try:
        magnitude = float(magnitude)
    except ValueError:
        print("\n[red][bold]Please enter a valid number for magnitude.[/bold][/red]")
        sleep(2)
        os.system("clear")
        sleep(1)
        continue

    angle = float(input("Enter the Angle of Force (Degree):  "))

    if angle > 180 or angle < -180:
        print("\n[red][bold]Please Enter Angles in The Right Way.[/bold][/red]")
        sleep(2)
        os.system("clear")
        sleep(1)
        continue

    magnitude_list.append(magnitude)
    angle_list.append(angle)

    os.system("clear")

os.system("clear")
sleep(1)

X = x_resultant(magnitude_list, angle_list)
Y = y_resultant(magnitude_list, angle_list)

resultant_magnitude = round(mp.sqrt(mp.power(X, 2) + mp.power(Y, 2)), 4)
resultant_angle = round(mp.degrees(mp.atan2(Y, X)), 4)

print(f"\nThe Resultant Force is a Vector With This Specifications :\n\nMagnitude : {resultant_magnitude} [italic]N[/italic]\nAngle : {resultant_angle} °\n\n\n")