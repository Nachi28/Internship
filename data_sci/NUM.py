import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read data from CSV file
data = pd.read_csv('marksque.csv')

names = data['Name'].tolist()
total = np.array(data['sub1'])+np.array(data['sub2'])+np.array(data['sub3'])

# Plotting


pass_fail = ['Pass' if i >= 120 else 'Fail' for i in total]
# print(total)
# print(pass_fail)

pass_color = 'green'
fail_color = 'red'

plt.bar(names, total)
plt.bar(names, total, color=[pass_color if pf == 'Pass' else fail_color for pf in pass_fail])
plt.ylim(0, 200)
# Customizing the plot
plt.title('Total Marks of Each Student')
plt.xlabel('Student Names')
plt.ylabel('Total Marks')

# Display the plot
plt.show()
