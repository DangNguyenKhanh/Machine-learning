Both decision tree and naive Bayes are widely used classification models in machine learning. While they are both used for classification tasks, they differ in their underlying assumptions and methodology. Here are some key differences between the two:

Assumptions: Naive Bayes assumes that the features are independent of each other, while decision tree does not make this assumption.

Training: Naive Bayes is a probabilistic model that estimates the probabilities of each class given the features. It uses a training dataset to estimate these probabilities. On the other hand, decision tree is a rule-based model that learns a set of if-then rules from the training data.

Performance: Naive Bayes is generally faster than decision tree because it requires less computational resources. However, decision tree can often achieve higher accuracy than Naive Bayes, especially when the dataset has complex relationships between the features and the class.

Interpretability: Decision tree models are more interpretable because they generate a set of if-then rules that can be easily understood by humans. Naive Bayes, on the other hand, can be difficult to interpret because it relies on complex probabilistic calculations.

In summary, the choice of model depends on the specific characteristics of the problem at hand. Naive Bayes is a good choice when there are many features and the dataset is large. Decision tree is a good choice when the dataset has complex relationships between the features and the class, and interpretability is important.

Dữ liệu phụ thuộc tức xuất hiện đồng thời với nhau: "Khanh" và "Tony" được coi là spam

Giả định: 2 tin nhắn "Khanh tony" coi là spam và 1 tin nhắn "tony" coi là ko spam thì phân loại nếu gặp tin nhắn chỉ tony không thì vẫn coi là spam. Giảm độ chính xác
 
