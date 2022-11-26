import matplotlib.pyplot as plt
from players import *


width = [1, 2, 3, 4, 5]

# Getting the sum of all the comments
total_tramaine = sum(tramaine)
total_spiro = sum(spiro)
total_oni = sum(oni_hasan)
total_jordan = sum(jordan)
total_luke = sum(luke)
  
# heights of bars
height = [total_tramaine, total_spiro, total_oni, total_jordan, total_luke]
  
# labels for bars
tick_label = ['Tramaine', 'Spiro', 'Oni Hasan', 'Jordan', 'Luke']
  
# plotting a bar chart
plt.bar(width, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])
  
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('Total comments that mention each player')
  
# function to show the plot
plt.show()