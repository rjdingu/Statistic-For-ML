import pandas as pd
data = pd.read_csv('D:\Statistic_ML\MeasureOfCentralTendency\Heart_Disease_Prediction.csv')
print(data)

mean = data['BP'].mean()
print(mean)

media= data['BP'].median()
print(media)


mode = data['BP Level'].mode()
print(mode)
