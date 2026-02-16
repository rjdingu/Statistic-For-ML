import pandas as pd

data = pd.read_csv('D:\Statistic_ML\Distribution\Heart_Disease_Prediction.csv')

# Find the data of BP is Right or Left Skew

mean = data['BP'].mean()
median = data['BP'].median()
mode = data['BP'].mode()[0]
'''
print(mean)
print(median)
print(mode)'''
if mean < median :
    if median < mode :
        print('It is Left Skew ')

if mode < median :
    if median < mean :
        print('It is Right skew')