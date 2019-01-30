# Dependencies 
# matplotlib for visualized the line

import matplotlib.pyplot as plt
# if we you jupyter note book then uncomment %matplotlib inline
#%matplotlib inline

# taking the points
x1 = float(input("Enter X1: "))
x2 = float(input("Enter X2: "))
y1 = float(input("Enter Y1: "))
y2 = float(input("Enter Y2: "))

# taking the absulute value for comparing
dx = abs(x2-x1)
dy = abs(y2-y1)

# take larger value as lenth
if dx >= dy:
    length = dx
else:
    length = dy

    
# this will make either dx or dy 1 because length is either dx or dy so incremented value of either x or y will be one
dx = (x2-x1)/length
dy = (y2-y1)/length

x = x1 + 0.5
y = y1 + 0.5
print(x,y)

i = 1
# to store the x and y points to plot
arr_x = []
arr_y = []
while i <= length:
    arr_x.append(int(x))
    arr_y.append(int(y))
    #print(int(x),int(y))
    x += dx # increment x
    y += dy # increment y
    print(x,y)
    i += 1
plt.plot(arr_x,arr_y) # plot the points
