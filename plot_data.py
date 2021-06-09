import global_vars as gva
import matplotlib.pyplot as plt
import numpy as np
import sys

indexLoopName = ''
TwUserName = []
x_value = []
y_value = []
tweets_max = []

for ix in range(len(gva.twUserArray)):
    indexLoopName = gva.twUserArray[ix]
    TwUserName.append(gva.twUserArray[ix])
    with open(indexLoopName + gva.twCounted, 'r', encoding='utf8') as file:
        dataSplitNewLine = file.read().splitlines()
        dataSplitSpace = [word for line in dataSplitNewLine for word in line.split()]
        file.close()
        # x-values
        x_value.append(dataSplitSpace[0])
        x_value.append(dataSplitSpace[2])
        x_value.append(dataSplitSpace[4])
        x_value.append(dataSplitSpace[6])
        x_value.append(dataSplitSpace[8])
        # y-values
        y_value.append(dataSplitSpace[1])
        y_value.append(dataSplitSpace[3])
        y_value.append(dataSplitSpace[5])
        y_value.append(dataSplitSpace[7])
        y_value.append(dataSplitSpace[9])
        # Max Tweets
        tweets_max.append(dataSplitSpace[10])

print(x_value)
print(y_value)
print(tweets_max)
print(TwUserName)

# loop
#for x2 in range(len(TwUserName)):
y_slice =
print(y_pop)

sys.exit(0)

# pyplot
x = np.arange(len(TwUserName))
width = 0.35

fig, ax = plt.subplots()
rect1 = ax.bar(x - width/2, y_pop[0], width)
rect2 = ax.bar(x + width/2 + 1, y_pop[1], width)
rect3 = ax.bar(x + width/2 + 2, y_pop[2], width)
rect4 = ax.bar(x + width/2 + 3, y_pop[3], width)
rect5 = ax.bar(x + width/2 + 4, y_pop[4], width)
