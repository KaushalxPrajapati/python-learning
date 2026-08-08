import math as m

def find_distance():
    dict1 = {}
    dict2 = {}

    # Input for point 2 (x2, y2, z2)
    for i in ['x2', 'y2', 'z2']:
        c = int(input("Enter the value of " + i + ": "))
        dict1[i] = c
    
    # Input for point 1 (x1, y1, z1)
    for i in ['x1', 'y1', 'z1']:
        c = int(input("Enter the value of " + i + ": "))
        dict2[i] = c

    # Extract coordinates from dictionaries
    x2, y2, z2 = dict1['x2'], dict1['y2'], dict1['z2']
    x1, y1, z1 = dict2['x1'], dict2['y1'], dict2['z1']

    # Calculate distance using the formula
    distance = m.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    
    print("The distance between the two points is:", distance)


find_distance()
