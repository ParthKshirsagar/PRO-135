import matplotlib.pyplot as plt
from storage import star_name, star_mass

plt.bar(star_name, star_mass)
plt.xlabel("Stars")
plt.ylabel("Mass")
plt.title("Star name vs Mass")
plt.show()