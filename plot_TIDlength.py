import matplotlib.pyplot as plt
import numpy as np


Coordinate=[100490358, 131840772, 13364415, 143761637, 143772893, 17197332, 190259587, 206302395, 239611933, 33777986, 48429116, 50456083, 66595428, 83167686, 8685810]
Length=[1036, 2585, 1015, 11228, 966, 114, 228, 240, 420, 486, 10049, 1420, 1773, 2119, 578]
points=[]
for i in range(0,15):
    points.append((Coordinate[i],Length[i]))
print(points)

plt.stem(Coordinate,Length)

# for pt in points:
#     # plot (x,y) pairs.
#     # vertical line: 2 x,y pairs: (a,0) and (a,b)
#     plt.plot( [pt[0],pt[0]], [0,pt[1]] )
plt.show()
