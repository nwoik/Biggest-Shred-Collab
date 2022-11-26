import matplotlib.pyplot as plt
from players import *
  

days = [1,2,3,4,5]

plt.plot(days, oni_hasan, label = "Oni Hasan")
  
plt.plot(days, tramaine, label = "Tramaine")

plt.plot(days, spiro, label = "Spiro")

plt.plot(days, jordan, label = "Jordan")

plt.plot(days, luke, label = "Luke")

# naming the x axis
plt.xlabel('Days')
# naming the y axis
plt.ylabel('Comments')
# giving a title to my graph
plt.title('Oni Hasan comments compared others from the contest')
  
# show a legend on the plot
plt.legend()
  
# function to show the plot
plt.show()