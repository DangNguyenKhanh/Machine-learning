import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# raw string
file_path = r"C:\Users\Admin\OneDrive - hcmut.edu.vn\Desktop\Books.xlsx"

# Load the data into a Pandas dataframe
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Drop the 'id' column
df = df.drop('id', axis=1)

# Convert categorical variables to numerical using one-hot encoding
df = pd.get_dummies(df, columns=['outlook', 'temperature', 'humidity', 'wind'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('play', axis=1), df['play'], test_size=0.2, random_state=42)

# Create the Multinomial Naive Bayes classifier
clf = MultinomialNB()

# Train the classifier
clf.fit(X_train, y_train)

# Test the classifier
accuracy = clf.score(X_test, y_test)
print(f'Accuracy: {accuracy:.2f}')      # 0.33
