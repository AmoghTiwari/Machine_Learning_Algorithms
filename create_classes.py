""" Script to create 2 linearly seperable classes"""

import numpy as np

def makeClasses():
	# Define parameters
	m=np.random.random()*5
	c=np.random.random()*10
	number_of_samples=100
	class1=[]
	class2=[]
	for i in range(number_of_samples):
		choice = np.random.choice([1,2])
		x = np.random.random()*20 - 10
		delta = np.random.random()*10
		if choice == 1:
			class1.append(m*x+c+delta)
		else:
			class2.append(m*x+c-delta)
	print("Equation of line is: y = %0.2fx + %0.2f"%(x,c))
	return class1, class2


if __name__ == "__main__":
	class1, class2 = makeClasses()
	print(len(class1))
	print(len(class2))
	m=np.random.random()*5
	c=np.random.random()*5
