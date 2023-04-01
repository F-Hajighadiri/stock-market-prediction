import numpy as np
import csv
import matplotlib.pyplot as plt

values_close = []

file = open("project_data.csv", 'r')
file_lines = file.readlines()
file.close()

for line in file_lines[1:] :
  data = line.split(',')
  values_close.append(float(data[5]))

plt.plot(values_close, label="values_close")

values_close = np.array(values_close)
dy = []
dy = values_close[1:] - values_close[:-1]   # dx = np.ones((...)) ->  deriv = dy/dx = dy

plt.plot(dy, label="Deriv")
plt.legend()


def split(arr, size):
  result = []
  while len(arr) > size :
    sub_arr = arr[:size]
    result.append(sub_arr)
    arr = arr[size:]
  result.append(arr)
  return result

sets = split(values_close, 10)

changes = []
for i in range(0, len(sets)-1) :
  if sets[i][9] < sets[i+1][0] :
    changes.append(True)
  else :
    changes.append(False)

print(changes)
plt.show()