# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 09:25:53 2023

@author: lqkvn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the source file
df = pd.read_csv("COVID19_Jan_3.csv")

plt.scatter(df.Date, df.Total_cases)

print (df.head)
x = np.arange(df['Date'].size)

fit = np.polyfit(x, df['Total_cases'], deg = 2)
print ("Slope : " + str(fit[0]))

#Fit function : y = mx + c [linear regression ]
fit_function = np.poly1d(fit)

#Linear regression plot
plt.plot(df['Date'], fit_function(x))
#Time series data plot
plt.plot(df['Date'], df['Total_cases'])

plt.title("COVID trend")
plt.xlabel('Date')
plt.ylabel('Cases')
plt.show()



