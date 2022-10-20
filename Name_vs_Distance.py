import matplotlib.pyplot as plt
from storage import star_name, star_distance

plt.bar(star_name, star_distance)
plt.xlabel("Stars")
plt.ylabel("Distance")
plt.title("Star name vs Distance")
plt.show()