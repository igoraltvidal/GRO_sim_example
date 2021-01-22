import matplotlib.pyplot as plt

class Group():
    def __init__(self):
        self.time = [0.0]
        self.value = [1]
    def print_data(self):
        print("Time", self.time)
        print("Value", self.value)

g1 = Group()
g2 = Group()
g3 = Group()
g4 = Group()

with open('data.txt') as input_file:
    for line in input_file.readlines ():
        data = line.split (' ')
        if(data[0] == 'group1'):
            g1.time.append(float(data[1]))
            g1.value.append(int(data[2]))
        elif(data[0] == 'group2'):
            g2.time.append(float(data[1]))
            g2.value.append(int(data[2]))
        elif(data[0] == 'group3'):
            g3.time.append(float(data[1]))
            g3.value.append(int(data[2]))
        else:
            g4.time.append(float(data[1]))
            g4.value.append(int(data[2]))

g1.print_data()
g2.print_data()
g3.print_data()
g4.print_data()


plt.plot(g1.time, g1.value, "r", label = "Group 1")
plt.plot(g2.time, g2.value, "g", label = "Group 2")
plt.plot(g3.time, g3.value, "c", label = "Group 3")
plt.plot(g4.time, g4.value, "y", label = "Group 4")


plt.locator_params(axis='x', nbins=10)
plt.xlabel('Time')
plt.ylabel('Number of cells')
plt.title('Number of cells evolution')
plt.legend()
plt.show()