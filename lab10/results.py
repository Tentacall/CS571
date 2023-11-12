import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data
leakyrelu_data = np.array([
    [10, 500, 29.299],
    [10, 1500, 31.75],
    [10, 1000, 27.38],
    [20, 1000, 33.87],
    [30, 1500, 38.23]
])

data = [
    [100, 10, 96.6],
    [100, 20, 100],
    [50, 20, 96.6],
    [50, 10, 86.6],
    [50, 5, 90],
    [100, 5, 96.6]
]

# Create a Pandas DataFrame for better handling
columns = ['Epochs', 'Num_Neurons', 'Accuracy']
# df = pd.DataFrame(leakyrelu_data, columns=columns)
df = pd.DataFrame(data, columns=columns)

# 3D Scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Epochs'], df['Num_Neurons'], df['Accuracy'], c='r', marker='o')

# Set labels
ax.set_xlabel('Epochs')
ax.set_ylabel('Num_Neurons')
ax.set_zlabel('Accuracy')

# Show plot
plt.show()
fig.savefig('iris_results_overall.png')
# fig.savefig('cifar_results_overall.png')

# Plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.plot(df['Num_Neurons'], df['Accuracy'], marker='o', linestyle='-')
ax.set_title('Number of Neurons vs. Accuracy')
ax.set_xlabel('Number of Neurons')
ax.set_ylabel('Accuracy')
plt.show()
fig.savefig('iris_results_num_nuerons.png')
# fig.savefig('cifar_results_num_nuerons.png')
