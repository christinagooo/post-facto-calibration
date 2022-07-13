import matplotlib.pyplot as plt
import numpy as np
import random

#the mask is static
mask = [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
#for this case, the count or cast "shadow" is an exact shadow of the mask
count = []

#Fills our count array perfectly. 10 signifies no x-ray hits
#100 signifies an x-ray hit
for x in range(len(mask)):
    if mask[x] == 0:
        count.append(10)
    else:
        count.append(100)

#Our cross correlation array
cc = np.correlate(mask, count, "full")

#Used only for the x axis of our mask and count graphs
xaxis = []
for x in range(len(mask)):
    xaxis.append(str(x + 1))

#Used only for the x axis of our cross correlation graph
xaxiscc = []
for x in range(len(cc)):
    xaxiscc.append(str(x + 1))

#Everything after this is plotting our graphs
figure, axis = plt.subplots(3)

axis[0].bar(xaxis, mask)
axis[0].set_title("Mask")

axis[1].bar(xaxis, count)
axis[1].set_title("Perfect Counts")

axis[2].bar(xaxiscc, cc)
axis[2].set_title("Cross Correlation")
axis[2].tick_params(axis='x', rotation=65)

figure.tight_layout()
figure.set_figheight(5)
figure.set_figwidth(25)
plt.show()
