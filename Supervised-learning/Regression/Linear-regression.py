from sklearn import linear_model    # regression
import numpy as np                  # array
import pandas as pd                 # excel
import matplotlib.pyplot as plt     # chart

# raw string
file_path = r"C:\Users\Admin\OneDrive - hcmut.edu.vn\Desktop\Books.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

height = np.empty((0, ))
weight = np.empty((0, ))

# row is adding to height
row = np.empty((0, ))
for i in range(len(df)):
    row = np.append(row, df.iloc[i][0])
    weight = np.append(weight, df.iloc[i][1])

# append a row to an array
height = np.append(height, [row])

# transposes the 2-D array, 1-D array doesn't work
height = np.array([height]).T

# create a model
regression = linear_model.LinearRegression()

# fit(input array, output array)
regression.fit(height, weight)

# plot the data points
plt.scatter(height, weight, color='blue')

# plot the linear regression line
plt.plot(height, regression.predict(height), color='red', linewidth=3)

# add axis labels and title
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Linear Regression of Height and Weight')

# print w_1, w_0 in formular y = w_1 * x + w_0
w_1 = regression.coef_[0]
w_0 = regression.intercept_
# f-string
print(f"The equation of the linear regression line is: y = {w_1:.2f}x + {w_0:.2f}")
h = 172
print(f"Predict weight of height: {h} is {(w_1 * h + w_0):.2f}")

# show the plot
plt.show()

