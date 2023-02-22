import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# raw string
file_path = r"C:\Users\Admin\OneDrive - hcmut.edu.vn\Desktop\Books.xlsx"

# Load the data into a Pandas dataframe
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Separate the categorical and numerical variables
categorical_vars = ['outlook', 'wind']
numerical_vars = ['temperature', 'humidity']

# Convert the categorical variables to numerical using one-hot encoding
categorical_df = pd.get_dummies(df[categorical_vars])

# Combine the one-hot encoded variables and the numerical variables into a single dataframe
X = pd.concat([categorical_df, df[numerical_vars]], axis=1)     # pd.concat([dataframe1, dataframe2], axis=1)
y = df['play']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Gaussian Naive Bayes classifier
clf = GaussianNB()

# Train the classifier using the training set
clf.fit(X_train, y_train)

# Predict the target values for the test set
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the model
accuracy = clf.score(X_test, y_test)
print(f'Accuracy: {accuracy:.2f}')
