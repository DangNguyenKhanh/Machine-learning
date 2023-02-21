# Decision tree - One-Hot Encoding (OHE) or One-of-K encoding
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# raw string
file_path = r"C:\Users\Admin\OneDrive - hcmut.edu.vn\Desktop\Books.xlsx"

# Load the data into a Pandas dataframe
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Dont use 'id' column
df = df.drop('id', axis=1)
features = df.drop('play', axis=1).columns

# Convert categorical variables to numerical using one-hot encoding
df = pd.get_dummies(df, columns=['outlook', 'temperature', 'humidity', 'wind'])     # [14 rows x 12 columns]

# Split the data into training and test sets
X = df.drop('play', axis=1)     # axis=1 -> col
y = df['play']

# option
option = 1
if option == 1:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
else:
    X_train = X
    y_train = y

# Train a decision tree classifier
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

# Make predictions on the test set
if option == 1:
    y_pred = dtc.predict(X_test)

    # # Evaluate the model performance
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))                      # (TP + TN) / (TP + TN + FP + FN)
    print("Precision:", metrics.precision_score(y_test, y_pred, pos_label='yes'))   # TP / (TP + FP)
    print("Recall:", metrics.recall_score(y_test, y_pred, pos_label='yes'))         # TP / (TP + FN)
    print("F1 Score:", metrics.f1_score(y_test, y_pred, pos_label='yes'))           # 2 * precision * recall / (precision + recall)

    # Accuracy: 0.4     40% dự đoán đúng
    # Precision: 1.0    100% dự đoán đúng FP = 0, không dự đoán sai thành đúng
    # Recall: 0.25      25% = 1 / (1 + 3) => FN = 3, 3 mẫu đúng nhưng phân vô nhãn sai
    # F1 Score: 0.4     low

elif option == 2:
    print("Enter values for the following features:")
    user_input = {}     # dict
    for feature in features:
        value = input(f"{feature}: ")
        user_input[feature] = value

    # Convert user input to a dataframe with a single row
    X_new = pd.DataFrame([user_input])

    # Convert categorical variables to numerical using one-hot encoding
    X_new = pd.get_dummies(X_new, columns=['outlook', 'temperature', 'humidity', 'wind'])

    # Reorder the columns to match the order of the original dataframe's columns
    X_new = X_new.reindex(columns=X.columns, fill_value=0)

    # Use the trained decision tree classifier to make a prediction on the new data point
    prediction = dtc.predict(X_new)
    print(f"Prediction: {prediction}")

else:
    user_input = {}  # dict
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
    prediction = dtc.predict(X_new)
    print(f"Prediction: {prediction}")
