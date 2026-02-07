import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("data/sample.csv")

# Basic analysis
print("Data preview:")
print(data.head())

print("\nAverage score:", data["score"].mean())
print("Max score:", data["score"].max())

# Plot score chart
plt.figure()
plt.plot(data["name"], data["score"], marker='o')
plt.title("Score Analysis")
plt.xlabel("Name")
plt.ylabel("Score")
plt.grid(True)
plt.show()