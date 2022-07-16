import matplotlib.pyplot as plt

fig = plt.figure(1)	#identifies the figure 
plt.title("Y vs X", fontsize='16')	#title
plt.plot([1, 2, 3, 4], [6,2,8,4])	#plot the points
plt.xlabel("X",fontsize='13')	#adds a label in the x axis
plt.ylabel("Y",fontsize='13')	#adds a label in the y axis
plt.legend(('YvsX'),loc='best')	#creates a legend to identify the plot
plt.savefig('Y_X.png')	#saves the figure in the present directory
plt.grid()	#shows a grid under the plot
plt.show()