> ID3
- used for both classification and regression problems.
- uses the information gain measure to select the splitting criterion for each node
- suited for small to medium-sized datasets with discrete features and a low number of class labels
- ID3 can easily overfit the training data and may not perform well on datasets with continuous features.
- Tại mọi nút (trừ leaf) có thể tạo nhiều hơn 2 nhánh -> đây là điểm chiến thắng CART về độ linh hoạt và đảm bảo chính xác

> C4.5
- an improved version of ID3
- ability to handle continuous features and missing values
- uses the gain ratio measure instead of information gain to select the splitting criterion for each node
- reduces the bias (thiên vị) towards features with many categories
- suited for medium to large-sized datasets with discrete or continuous features and a low to moderate number of class labels.

> CART (Classification and Regression Tree)
- handle both classification(chính) and regression problems with discrete or continuous features
- uses the Gini impurity measure to select the splitting criterion for each node
- suited for datasets with a large number of features and a moderate to large number of samples.
- Tại mọi nút chỉ tạo ra 2 nhánh (nhị phân)

> One-hot encoding
- Không phải là decision tree algorithm, là kĩ thuật tiền xử lí (preprocessing technique)
- suited for categorical features with a moderate (trung bình) number of categories

> Đánh giá (evaluate)
- Accuracy: tỉ lệ các trường hợp được phân loại đúng trên tổng số các trường hợp trong tập kiểm tra.
- Precision: tỉ lệ số lượng dự đoán đúng nhãn positive so với tổng số lượng các trường hợp được dự đoán là positive.
- Recall: tỉ lệ số lượng dự đoán đúng nhãn positive so với tổng số lượng các trường hợp thực sự là positive.
- F1 score: giá trị trung bình điều hòa giữa Precision và Recall, cho trọng số bằng nhau cho cả hai chỉ số.
