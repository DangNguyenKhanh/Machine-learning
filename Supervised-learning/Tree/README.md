> ID3
- uses the information gain measure to select the splitting criterion for each node
- suited for small to medium-sized datasets with discrete features and a low number of class labels
- ID3 can easily overfit the training data and may not perform well on datasets with continuous features.

> C4.5
- an improved version of ID3
- ability to handle continuous features and missing values
- uses the gain ratio measure instead of information gain to select the splitting criterion for each node
- reduces the bias (thiên vị) towards features with many categories
- suited for medium to large-sized datasets with discrete or continuous features and a low to moderate number of class labels.

> CART (Classification and Regression Tree)
- handle both classification and regression problems with discrete or continuous features
- uses the Gini impurity measure to select the splitting criterion for each node
- suited for datasets with a large number of features and a moderate to large number of samples.

> One-hot encoding
- Không phải là decision tree algorithm, là kĩ thuật tiền xử lí (preprocessing technique)
- suited for categorical features with a moderate (trung bình) number of categories