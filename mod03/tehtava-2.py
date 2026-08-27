import math

# Kysyy säteen
circle_radius = int(input("Anna ympyrän säde: "))

# Laskee pinta-alan
circle_area = math.pi * pow(circle_radius, 2)

# Tulostaa käyttäjälle pinta-alan
print(f"Ympyrän pinta-ala: {circle_area:.1f}")