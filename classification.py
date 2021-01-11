from math import random

def createClasses():
	# Define parameters
	m=random.random()*5
	c=random.random()*10
	number_of_samples=100
	class1=[]
	class2=[]
	for i in range(number_of_samples):
		choice = random.choice([1,2])
		x = random.random()*20 - 10
		delta = random.random()*10
		if choice == 1:
			class1.append(m*x+c+delta)
		else:
			class2.append(m*x+c-delta)
	print("Equation of line is: y = %0.2fx + %0.2f"%(x,c))
	return class1, class2

if __name__ == "__main__":
	class1, class2 = createClasses()
	print(len(class1))
	print(len(class2))
	m=random.random()*5
	c=random.random()*5
