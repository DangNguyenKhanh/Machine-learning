from sklearn import linear_model    # regression
import numpy as np                  # array
import pandas as pd                 # excel
import matplotlib.pyplot as plt     # chart
import math as m                    # math

# raw string
file_path = r"C:\Users\Admin\OneDrive - hcmut.edu.vn\Desktop\Books1.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# read datas from excel
time = np.array(df['Time']).reshape(-1, 1)      # col = 1, option = -1 -> guess row
achieved = np.array(df['Achieved'])

# create a model
logistic_regression = linear_model.LogisticRegression()

# train model by fit(input array2D, output array1D)
logistic_regression.fit(time, achieved)

# plot the data points
plt.scatter(time, achieved, color='blue', )

# option print plot
option = 1

# plot logistic regression line
if option == 1:     # data is sorted, if not it will print many line
    # return array2D([[negative-class, positive-class],
    #                 [non-target-class, target-class],
    #                 [0.3, 0.7]])
    probabilities = logistic_regression.predict_proba(time)
    # probabilities[:, 1] selects target class as an array
    plt.plot(time, probabilities[:, 1], color='red', linewidth=3)
else:
    # Clearly plot than option 1
    x_min, x_max = time.min(), time.max()
    # creates a one-dimensional array of 100 equally spaced numbers between x_min and x_max
    x_values = np.linspace(x_min, x_max, 100).reshape(-1, 1)            # 2D array of 100 elements equally spaced
    y_values = logistic_regression.predict_proba(x_values)[:, 1]        # 1D array
    plt.plot(x_values, y_values, color='red', linewidth=2)

# add axis labels and title
plt.xlabel('Time study')
plt.ylabel('Achieved')
plt.title('Logistic Regression of Time study and Achieved')

# p = 1 / (1 + e^-(a0 + a1x1 + a2x2 + ...))
w_1 = logistic_regression.coef_[0][0]       # [[a1]]
w_0 = logistic_regression.intercept_[0]     # [a0]

# format-string
print(f"The equation of the logistic regression line is: y = 1 / (1 + e^-({w_0:.2f} + {w_1:.2f}x)")

# predict the probability of achieving for a study time
t = 3
prob_pass = logistic_regression.predict_proba([[t]])[:, 1][0]   # [[t]] -> [[neg, pos]] -> [pos] -> pos
print(f"Predict probability of achieving for study time {t} is {prob_pass:.2f}")
print(f"Calculate non-using model: {1 / (1 + m.exp(-w_0 - w_1 * t))}")

# show the plot
plt.show()
