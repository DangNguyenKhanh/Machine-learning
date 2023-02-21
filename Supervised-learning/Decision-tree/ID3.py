import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# raw string
file_path = r"C:\Users\Admin\OneDrive - hcmut.edu.vn\Desktop\Books.xlsx"

# Load the data into a Pandas dataframe
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Drop the 'id' column
df = df.drop('id', axis=1)

# Convert categorical variables to numerical using one-hot encoding
df = pd.get_dummies(df, columns=['outlook', 'temperature', 'humidity', 'wind'])

# Split the data into training and test sets
X = df.drop('play', axis=1)
y = df['play']
X_train = X
y_train = y

# Train a decision tree classifier using the ID3 algorithm
dtc = DecisionTreeClassifier(criterion="entropy")
dtc.fit(X_train, y_train)

# Make a prediction on a new data point using the trained ID3 decision tree classifier
user_input = {}
user_input['outlook'] = 'sunny'
user_input['temperature'] = 'hot'
user_input['humidity'] = 'high'
user_input['wind'] = 'strong'

# Convert user input to a dataframe with a single row
X_new = pd.DataFrame([user_input])

# Convert categorical variables to numerical using one-hot encoding
X_new = pd.get_dummies(X_new, columns=['outlook', 'temperature', 'humidity', 'wind'])

# Reorder the columns to match the order of the original dataframe's columns
X_new = X_new.reindex(columns=X.columns, fill_value=0)

# Use the trained decision tree classifier to make a prediction on the new data point
y_pred = dtc.predict(X_new)
print(f"Prediction: {y_pred}")

# split to train data and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# predict
y_pred = dtc.predict(X_test)

# # Evaluate the model performance
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))  # (TP + TN) / (TP + TN + FP + FN)
print("Precision:", metrics.precision_score(y_test, y_pred, pos_label='yes'))  # TP / (TP + FP)
print("Recall:", metrics.recall_score(y_test, y_pred, pos_label='yes'))  # TP / (TP + FN)
print("F1 Score:", metrics.f1_score(y_test, y_pred, pos_label='yes'))  # 2 * precision * recall / (precision + recall)

# output
    # Prediction: ['no']
    # Accuracy: 1.0
    # Precision: 1.0
    # Recall: 1.0
    # F1 Score: 1.0
