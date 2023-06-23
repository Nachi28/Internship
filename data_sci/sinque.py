import matplotlib.pyplot as plt
import numpy as np

angles = np.arange(0, 8 * np.pi + np.pi / 2, np.pi / 2)


values= np.arange(len(angles)) % 2
# print(values)

plt.plot(angles, values)

plt.title('Angles and Values')
plt.xlabel('Angle')
plt.ylabel('Value')
plt.xticks(angles) 

plt.show()
