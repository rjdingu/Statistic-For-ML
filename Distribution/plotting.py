import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('D:\Statistic_ML\Distribution\Heart_Disease_Prediction.csv')

plt.hist(data['BP'] , bins = 10)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Distribution of BP from HealthCare Data')
plt.show()





plt.hist(data['Cholesterol'] , bins = 10)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Distribution of Cholestrerol from HealthCare Data')
plt.show()