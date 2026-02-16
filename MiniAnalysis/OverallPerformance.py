import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv("D:\Statistic_ML\MiniProject\GHI_Report.csv")
print("Description : ")
print(data.describe())

print("Information : ")
print(data.info())
print("Correlation : ")

print(data.corr())


def plot(a,b,c,d):
    plt.scatter(a , b)
    plt.title(" Visualisation")
    plt.xlabel(c)
    plt.ylabel(d)
    plt.show()

x = 'Economy'
y = 'H_Score'
c = data[x]
d = data[y]

plot(c,d,x,y)
    

