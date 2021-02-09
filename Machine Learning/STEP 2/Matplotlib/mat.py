# video one on simple line plot
from matplotlib import pyplot  as plt
import numpy as np

age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 64920, 62316, 67317, 68748, 73752]

plt.title('Median salary by age')

plt.xlabel('Age')

plt.ylabel('Median salary')



# adding color and label, normal way
#plt.plot(age_x, dev_y, 'k--', label='All Dev')

# passing the the color and linestyle and marker as argument
#plt.plot(age_x, dev_y, color ='r', linestyle='--',  marker= '.', label='All Dev')

# You can add hex color values to make it look nicer
plt.plot(age_x, dev_y, color ='#444444', linestyle='--',  marker= '.', label='All Dev')

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]


# adding label and color
#plt.plot(age_x, py_dev_y, 'b', label='Python')

# addding color and linestyle and marker as argument
#plt.plot(age_x, py_dev_y, color='b', marker='o', label='Python')

plt.plot(age_x, py_dev_y, color='#5a7d9a', marker='o', label='Python')

# added javascript snippet
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(age_x, js_dev_y, color='#adad3b', marker='*', label='Javascript')


plt.legend()
plt.show()


