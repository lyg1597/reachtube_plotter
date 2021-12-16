from plotter.plotter2D import plot
from plotter.parser import Parser
import matplotlib.pyplot as plt 

f = open('./reachtube_billiard.txt','r')
parser1 = Parser(f)
data = parser1.get_all_data()
fig = plot(data, 1, [2])
plt.show()
