import pandas as pd
import matplotlib as mtp

data = pd.read_csv('D:\Statistic_ML\Distribution\Heart_Disease_Prediction.csv')


freq_bp = data['BP'].value_counts()

freq_Choles = data['Cholesterol'].value_counts()

freq_Age = data['Age'].value_counts


