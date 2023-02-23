# Multilayer Feedforward Neural Network
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
# from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# raw string
file_path = r"C:\Users\Admin\OneDrive - hcmut.edu.vn\Desktop\Books.xlsx"

# Load the data into a Pandas dataframe
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Convert categorical data to numerical data
encoder = LabelEncoder()
df['outlook'] = encoder.fit_transform(df['outlook'])
df['wind'] = encoder.fit_transform(df['wind'])
df['play'] = encoder.fit_transform(df['play'])

# Split the data into training and testing sets
X = df.drop(['id', 'play'], axis=1)
y = df['play']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network architecture
model = Sequential([
    Dense(4, activation='relu', input_shape=(4,)),
    Dense(4, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=1)

# Evaluate the model on the testing set
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {accuracy:.2f}')     # 0.67


