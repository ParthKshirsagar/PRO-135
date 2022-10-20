import matplotlib.pyplot as plt
from storage import star_name, star_radius

plt.bar(star_name, star_radius)
plt.title("Star name vs Radius")
plt.xlabel("Stars")
plt.ylabel('Radius')
plt.show()