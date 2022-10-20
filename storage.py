import csv
with open('final.csv') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)

headers = data[0]
all_stars = data[1:]

star_mass = []
star_name = []
star_radius = []
star_distance = []
star_gravity = []

for star in all_stars:
    star_mass.append(star[2])
    star_name.append(star[0])
    star_radius.append(star[3])
    star_distance.append(star[1])
    star_gravity.append(star[8])