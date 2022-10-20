import matplotlib.pyplot as plt
from storage import star_name, star_gravity

plt.bar(star_name, star_gravity)
plt.xlabel("Stars")
plt.ylabel("Gravity")
plt.title("Star name vs Gravity")
plt.show()