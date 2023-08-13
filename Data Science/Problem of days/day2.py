import math

def cone_volume(height, radius):
    if height <= 0 or radius <= 0:
        raise ValueError("Height and radius must be positive values.")
    
    volume = (1/3) * math.pi * radius**2 * height
    return volume



cone_height = float(input("Enter the height of the cone: "))
cone_radius = float(input("Enter the radius of the cone's base: "))
    
volume = cone_volume(cone_height, cone_radius)
print("Volume of the cone:", volume)
 
