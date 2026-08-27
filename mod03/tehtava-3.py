# Kysyy käyttäjältä kannan sekä korkeuden
rectangle_base = int(input("Anna suorakulmion kanta: "))
rectangle_height = int(input("Anna suorakulmion korkeus: "))

# Laskee piirin sekä pinta-alan
rect_perimeter = rectangle_base * 2 + rectangle_height * 2
rect_area = rectangle_base * rectangle_height

# Tulostaa tulokset
print(f"Suorakulmion piiri: {rect_perimeter}\nSuorakulmion pinta-ala: {rect_area}")