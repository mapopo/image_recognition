from PIL import Image
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
import time


def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in newAr:
        for eachPixle in eachRow:
            avgNum = reduce(lambda x, y: x + y, eachPixle[:3])/len(eachPixle[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr)/len(balanceAr)

    for eachRow in newAr:
        for eachPixle in eachRow:
            if reduce(lambda x, y: x + y, eachPixle[:3])/len(eachPixle[:3]) > balance:
                eachPixle[0] = 255
                eachPixle[1] = 255
                eachPixle[2] = 255
                eachPixle[3] = 255
            else:
                eachPixle[0] = 0
                eachPixle[1] = 0
                eachPixle[2] = 0
                eachPixle[3] = 255
    return newAr


i = Image.open('images/numbers/0.1.png')
iAr = np.array(i)

i2 = Image.open('images/numbers/y0.4.png')
iAr2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iAr3 = np.array(i3)

i4 = Image.open('images/002.png')
iAr4 = np.array(i4)

threshold(iAr)
threshold(iAr2)
threshold(iAr3)
#threshold(iAr4)


fig = plt.figure()
ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8, 6), (4, 3), rowspan=4, colspan=3)

ax1.imshow(iAr)
ax2.imshow(iAr2)
ax3.imshow(iAr3)
ax4.imshow(iAr4)
