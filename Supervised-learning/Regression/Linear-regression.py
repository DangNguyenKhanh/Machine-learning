from sklearn import linear_model
import numpy as np
import pandas as pd

# taking data from excel
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

# print w_1, w_0 in formular y = w_1 * x + w_0
w_1 = regression.coef_[0]
w_0 = regression.intercept_
print("Solution of w_1:", w_1, "w_0:", w_0)
h = 172
print("Predict weight of height:", h, "is", w_1 * h + w_0)


